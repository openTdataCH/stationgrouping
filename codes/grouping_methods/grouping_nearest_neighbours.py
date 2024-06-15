import csv
import os
from shapely.geometry import Point
from difflib import SequenceMatcher
from sklearn.neighbors import NearestNeighbors
import geopandas as gpd
from shapely.ops import transform
import pyproj
import numpy as np
from colorama import Fore

def remove_duplicates_from_list(input_list):
    unique_list = []
    [unique_list.append(i) for i in input_list if i not in unique_list]
    return unique_list

def merge_overlapping_lists(station_connections):
    merged_connections = []
    for connection in station_connections:
        found_match = False
        for existing_connection in merged_connections:
            if any(name in existing_connection for name in connection):
                existing_connection.extend(connection)
                found_match = True
                break
        if not found_match:
            merged_connections.append(connection)
    return merged_connections

def transform_to_epsg2056(geometry):
    transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:2056", always_xy=True)
    x, y = transformer.transform(geometry.x, geometry.y)
    return Point(x, y)

def preprocess_name(name):
    return name.replace("strasse", "").strip()

def calculate_distance(point1, point2):
    return np.sqrt(np.sum((np.array([point1.x, point1.y]) - np.array([point2.x, point2.y]))**2))

def is_valid_coordinate(value):
    try:
        float_value = float(value)
        return np.isfinite(float_value)
    except ValueError:
        return False

def grouping_nearest_neighbours(similarity_distance_threshold_m, distance_threshold_m, similarity_threshold):
    print("---Grouping stations with nearest neighbours method")
    station_connections = []
    station_attributes = {}
    count = 1

    # Einlesen der Stationen und ihrer Koordinaten
    stations = []
    no_coord_stations = []
    rejected_stations = []
    with open(f"data/merged/stations_merged.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        pos_nr = 0
        for element in header:
            if element == "name_official":
                pos_name = pos_nr
            if element == "wgs84_e":
                pos_east = pos_nr
            if element == "wgs84_n":
                pos_north = pos_nr
            pos_nr += 1
        for line in reader:
            parts = line
            name = parts[pos_name]
            lon = parts[pos_east]
            lat = parts[pos_north]
            if is_valid_coordinate(lon) and is_valid_coordinate(lat):
                try:
                    lon = float(lon)
                    lat = float(lat)
                    stations.append((name, lon, lat, parts))
                except ValueError as e:
                    print(Fore.RED + f"Error converting coordinates: {lon}, {lat}. Error: {e}" + Fore.RESET)
                    no_coord_stations.append(parts)
                    rejected_stations.append(parts)
            else:
                if lon == "":
                    lon = "None"
                if lat == "":
                    lat = "None"
                print(Fore.RED + f"Invalid coordinates for station {name}: lon = {lon}, lat = {lat}" + Fore.RESET)
                no_coord_stations.append(parts)
                rejected_stations.append(parts)

    print(f"Total stations: {len(stations + no_coord_stations)}")
    print(f"Valid stations: {len(stations)}")
    print(f"Stations without valid coordinates: {len(no_coord_stations)}")

    # Erstellen eines GeoDataFrames
    gdf = gpd.GeoDataFrame(stations, columns=['name', 'lon', 'lat', 'attributes'])
    gdf['geometry'] = gdf.apply(lambda row: Point(row['lon'], row['lat']), axis=1)
    gdf = gdf.set_geometry('geometry')

    # Transformieren der Koordinaten in EPSG:2056 für genaue Distanzberechnungen
    gdf['geometry_epsg2056'] = gdf['geometry'].apply(transform_to_epsg2056)

    # Verwenden von NearestNeighbours, um die nächsten Nachbarn zu finden
    coords_epsg2056 = gdf['geometry_epsg2056'].apply(lambda geom: [geom.x, geom.y]).tolist()
    
    # Überprüfen, ob alle Koordinaten gültig sind und nur gültige Stationen verwenden
    valid_stations = []
    valid_coords_epsg2056 = []
    for station, coord in zip(stations, coords_epsg2056):
        if np.isfinite(coord[0]) and np.isfinite(coord[1]):
            valid_stations.append(station)
            valid_coords_epsg2056.append(coord)
        else:
            rejected_stations.append(station[3])
            print(f"Rejected station due to invalid EPSG:2056 coordinates: {station}")

    #print(f"Valid stations: {len(valid_stations)}")

    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(valid_coords_epsg2056)
    distances, indices = nbrs.kneighbors(valid_coords_epsg2056)

    # Gruppenbildung basierend auf den nächsten Nachbarn und Namensähnlichkeit
    for idx, station in enumerate(valid_stations):
        name_1 = preprocess_name(station[0])
        name_1_list = name_1.split()
        if len(name_1_list) > 1:
            name_1_wc = " ".join(name_1_list[1:])  # Erstellen des Wildcard-Namens für name_1
        else:
            name_1_wc = name_1  # Falls nur ein Wort vorhanden ist, dieses Wort verwenden

        nearest_neighbors = indices[idx][1:]  # Die nächsten Nachbarn (ohne sich selbst)
        connection = [(station[0], station[1], station[2])]  # Tuple aus (Name, lon, lat)

        for neighbor_idx in nearest_neighbors:
            name_2 = preprocess_name(valid_stations[neighbor_idx][0])
            name_2_list = name_2.split()
            if len(name_2_list) > 1:
                name_2_wc = " ".join(name_2_list[1:])  # Erstellen des Wildcard-Namens für name_2
            else:
                name_2_wc = name_2  # Falls nur ein Wort vorhanden ist, dieses Wort verwenden
            name_similarity = SequenceMatcher(None, name_1_wc, name_2_wc).ratio()

            # Prüfen, ob die Distanz kleiner als der Schwellenwert ist
            distance = calculate_distance(
                Point(valid_coords_epsg2056[idx]), 
                Point(valid_coords_epsg2056[neighbor_idx])
            )
            if distance <= distance_threshold_m or (name_similarity >= similarity_threshold and distance <= similarity_distance_threshold_m):
                connection.append((valid_stations[neighbor_idx][0], valid_stations[neighbor_idx][1], valid_stations[neighbor_idx][2]))

        station_connections.append(connection)
        station_attributes[(station[0], station[1], station[2])] = station[3]
        count += 1

    #print(f"Initial station connections: {len(station_connections)}")

    # Fusionieren der überlappenden Listen
    merged_station_connections = merge_overlapping_lists(station_connections)

    print(f"Metastation count: {len(merged_station_connections)}")

    # Entfernen von Duplikaten innerhalb jeder Subliste
    cleaned_station_connections = [remove_duplicates_from_list(connection) for connection in merged_station_connections]

    # Erstellen der erweiterten Datensätze mit metastation_id
    extended_station_data = []
    metastation_id = 1
    seen_stations = set()
    for connection in cleaned_station_connections:
        for station in connection:
            if (station[0], station[1], station[2]) not in seen_stations:
                attributes = station_attributes.get((station[0], station[1], station[2]), [])
                extended_station_data.append(attributes + [metastation_id])
                seen_stations.add((station[0], station[1], station[2]))
        metastation_id += 1

    # Hinzufügen der Stationen ohne Koordinaten mit eigenen metastation_id
    for station in no_coord_stations:
        extended_station_data.append(station + [metastation_id])
        metastation_id += 1

    # Speichern der erweiterten Datensätze in eine CSV-Datei
    new_file_path = os.path.join("data/grouped/grouping_nearest_neighbours.csv")
    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(header + ['metastation_id'])
        for element in extended_station_data:
            if len(element) > 10:
                writer.writerow(element)

    print(f"Total output stations: {len(extended_station_data)}")
    print(f"Saved grouped data in {new_file_path}")

    # Speichern der ungültigen Datensätze in eine CSV-Datei
    rejected_file_path = os.path.join("data/grouped/grouping_nearest_neighbours_rejected.csv")
    with open(rejected_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(header)
        for element in rejected_stations:
            if len(element) > 10:
                writer.writerow(element)

    print(f"Saved not valid stations in {rejected_file_path}")