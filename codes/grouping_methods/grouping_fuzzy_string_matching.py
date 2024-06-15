import csv
import os
from shapely.geometry import Point
from fuzzywuzzy import fuzz
import geopandas as gpd
import pyproj
from shapely.ops import transform

def transform_to_epsg2056(geometry):
    project = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:2056", always_xy=True).transform
    return transform(project, geometry)

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

def preprocess_name(name):
    name_parts = name.split()
    if len(name_parts) > 1:
        return " ".join(name_parts[1:])
    return name

def grouping_fuzzy(similarity_dist_max, dist_max, similarity_dist_middle, dist_middle, similarity_dist_min, dist_min, name_start):
    print("---Grouping stations with the fuzzy-string-matching method")
    station_connections = []
    station_attributes = {}
    count = 1

    stations = []
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
            if parts[pos_east] != '':
                if name.startswith(name_start):
                    lon = float(parts[pos_east])
                    lat = float(parts[pos_north])
                    stations.append((name, lon, lat, parts))

    gdf = gpd.GeoDataFrame(stations, columns=['name', 'lon', 'lat', 'attributes'])
    gdf['geometry'] = gdf.apply(lambda row: Point(row['lon'], row['lat']), axis=1)
    gdf = gdf.set_geometry('geometry')
    gdf['geometry_epsg2056'] = gdf['geometry'].apply(transform_to_epsg2056)

    for idx, station in enumerate(stations):
        name_1 = preprocess_name(station[0])
        connection = [station[0]]

        for idx_2, station_2 in enumerate(stations):
            if idx != idx_2:
                name_2 = preprocess_name(station_2[0])
                name_similarity = fuzz.ratio(name_1, name_2) / 100.0
                distance = gdf.iloc[idx]['geometry_epsg2056'].distance(gdf.iloc[idx_2]['geometry_epsg2056'])

                if (name_similarity >= similarity_dist_max and distance <= dist_max) or \
                   (name_similarity >= similarity_dist_middle and distance <= dist_middle) or \
                   (name_similarity >= similarity_dist_min and distance <= dist_min):
                    connection.append(station_2[0])

        station_connections.append(connection)
        station_attributes[station[0]] = station[3]
        print(f"{count} completed")
        count += 1

    merged_station_connections = merge_overlapping_lists(station_connections)
    cleaned_station_connections = [remove_duplicates_from_list(connection) for connection in merged_station_connections]

    extended_station_data = []
    metastation_id = 1
    for connection in cleaned_station_connections:
        for station in connection:
            attributes = station_attributes.get(station, [])
            extended_station_data.append(attributes + [metastation_id])
        metastation_id += 1

    new_file_path = os.path.join("data/grouped/grouping_fuzzy.csv")
    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(header + ['metastation_id'])
        for element in extended_station_data:
            if len(element) > 10:
                writer.writerow(element)

    print(f"saved file as {new_file_path}")