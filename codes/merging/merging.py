import csv
import glob
import os
from datetime import datetime

def merge_data():
    print("---Merging data")
    
    csv_files = glob.glob('data/read/*.csv')

    base_file = 'stations.csv'
    if base_file in csv_files:
        csv_files.remove(base_file)
        csv_files.insert(0, base_file)

    all_data = []
    unique_id_fields = set()
    static_fields = ['name_official', 'name_long', 'name_short', 'name_alternative', 
                    'lang', 'stations_metastation', 'wgs84_e', 'wgs84_n', 'wgs84_h', 
                    'wgs84_epsg', 'local_e', 'local_n', 'local_h', 'local_epsg',
                    'station_priority', 'km_info', 'stations_metastation_hrdf']

    for file in csv_files:
        with open(file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            headers = reader.fieldnames
            id_fields = [col for col in headers if col.startswith('id_')]
            unique_id_fields.update(id_fields)

            for row in reader:
                if os.path.basename(file) != base_file:
                    row['source_file'] = os.path.basename(file).replace('.csv', '')
                row['timestamp'] = datetime.now().isoformat() if os.path.basename(file) != base_file else row['timestamp']
                all_data.append(row)

    all_fields = list(unique_id_fields) + static_fields + ['source_file', 'timestamp']

    for row in all_data:
        for field in all_fields:
            if field not in row:
                row[field] = None

    seen = {}
    for row in all_data:
        coord = (row['wgs84_e'], row['wgs84_n'], row['name_official'])
        if coord not in seen:
            seen[coord] = row
        else:
            if seen[coord]['source_file'] == base_file:
                continue
            else:
                conflicting = False
                for id_field in unique_id_fields:
                    if row[id_field] and seen[coord][id_field] and row[id_field] != seen[coord][id_field]:
                        conflicting = True
                        break
                if conflicting:
                    continue
                else:
                    for id_field in unique_id_fields:
                        if row[id_field]:
                            if seen[coord][id_field]:
                                existing_ids = set(seen[coord][id_field].split(', '))
                                new_ids = set(row[id_field].split(', '))
                                combined_ids = ', '.join(existing_ids.union(new_ids))
                                seen[coord][id_field] = combined_ids
                            else:
                                seen[coord][id_field] = row[id_field]

    with open('data/merged/stations_merged.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_fields, delimiter=';')
        writer.writeheader()
        writer.writerows(seen.values())
    with open('data/read/stations.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_fields, delimiter=';')
        writer.writeheader()
        writer.writerows(seen.values())

    print('Data successfully merged')