import csv
from shapely.geometry import Point
from difflib import SequenceMatcher
import os
import geopandas

def create_buffer(lon, lat, radius_meters):
    point_wgs84 = Point(lon, lat)
    gdf = geopandas.GeoDataFrame(geometry=[point_wgs84], crs="EPSG:4326")
    gdf_lv95 = gdf.to_crs(epsg=2056)
    buffer_lv95 = gdf_lv95.geometry.buffer(radius_meters)
    buffer_wgs84 = buffer_lv95.to_crs(epsg=4326)
    return buffer_wgs84

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

def grouping_buffer(buffer_1_r_m, buffer_2_r_m, buffer_3_r_m, similarity_1, similarity_2, name_start):
    print("---Grouping stations with buffer method")
    station_connections = []
    station_attributes = {}
    count = 1

    print("Reading stations and their coordinates")
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
            name_1 = parts[pos_name]
            attributes = parts

            name_1_list = name_1.split()
            name_1_wc = "".join(name_1_list[1:])
            if "strasse" in name_1:
                name_1 = name_1.replace("strasse", "")

            if name_1.startswith(name_start):
                if parts[pos_east] == '':
                    station_connections.append([name_1])
                else:
                    long = float(parts[pos_east])
                    lat = float(parts[pos_north])
                    station_connections.append([name_1])
                    buffer1 = create_buffer(long, lat, buffer_1_r_m)
                    buffer2 = create_buffer(long, lat, buffer_2_r_m)
                    buffer3 = create_buffer(long, lat, buffer_3_r_m)
                    with open(f"data/merged/stations_merged.csv", "r") as file_2:
                        reader_2 = csv.reader(file_2, delimiter=';')
                        next(reader_2)
                        for line_2 in reader_2:
                            parts_2 = line_2
                            name_2 = parts_2[pos_name]
                            if "strasse" in name_2:
                                name_2 = name_2.replace("strasse", "")
                            if name_2 == name_1:
                                pass
                            elif parts_2[pos_east] == '':
                                pass
                            else:
                                long_2 = float(parts_2[pos_east])
                                lat_2 = float(parts_2[pos_north])
                                point = Point(long_2, lat_2)
                                if point.within(buffer1.geometry[0]):
                                    name_2_list = name_2.split()
                                    name_2_wc = " ".join(name_2_list[1:])
                                    name_similarity = SequenceMatcher(None, name_1_wc, name_2_wc)
                                    if round(name_similarity.ratio(), 2) >= similarity_1:
                                        station_connections[-1].append(name_2)
                                if name_2 not in station_connections[-1]:
                                    if point.within(buffer2.geometry[0]):
                                        name_2_list = name_2.split()
                                        name_2_wc = " ".join(name_2_list[1:])
                                        name_similarity = SequenceMatcher(None, name_1_wc, name_2_wc)
                                        if round(name_similarity.ratio(), 2) >= similarity_2:
                                            station_connections[-1].append(name_2)
                                if name_2 not in station_connections[-1]:
                                    if point.within(buffer3.geometry[0]):
                                        station_connections[-1].append(name_2)
                    station_attributes[name_1] = attributes
                    if count % 50 == 0:
                        print(f"{count} stations grouped")
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

    new_file_path = os.path.join("data/grouped/grouping_buffer.csv")
    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(header + ['metastation_id'])
        for element in extended_station_data:
            if len(element) > 10:
                writer.writerow(element)
    
    print(f"Total output stations: {len(extended_station_data)}")
    print(f"Saved grouped data in {new_file_path}")
