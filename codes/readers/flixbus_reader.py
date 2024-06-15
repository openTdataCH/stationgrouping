import xml.etree.ElementTree as ET
import csv

namespaces = {
    'netex': 'http://www.netex.org.uk/netex',
    'gml': 'http://www.opengis.net/gml/3.2',
    'siri': 'http://www.siri.org.uk/siri'
}

tree = ET.parse('data/EPIP-NeTEx_FLIXBUS_20230607.xml')
root = tree.getroot()

data_main = {}

frame_defaults = root.find('.//netex:FrameDefaults', namespaces)
if frame_defaults is not None:
    locale = frame_defaults.find('netex:DefaultLocale', namespaces)
    if locale is not None:
        data_main['lang'] = locale.find('netex:DefaultLanguage', namespaces).text if locale.find('netex:DefaultLanguage', namespaces) is not None else ''
    data_main['wgs84_epsg'] = frame_defaults.find('netex:DefaultLocationSystem', namespaces).text if frame_defaults.find('netex:DefaultLocationSystem', namespaces) is not None else ''

stop_places = []
quays = []

for stop_place in root.findall('.//netex:StopPlace', namespaces):
    stop_place_data = {
        'id_fli': stop_place.attrib.get('id', ''),
        'name_official': stop_place.find('netex:Name', namespaces).text if stop_place.find('netex:Name', namespaces) is not None else '',
        'wgs84_e': round(float(stop_place.find('netex:Centroid/netex:Location/netex:Longitude', namespaces).text), 6) if stop_place.find('netex:Centroid/netex:Location/netex:Longitude', namespaces) is not None else '',
        'wgs84_n': round(float(stop_place.find('netex:Centroid/netex:Location/netex:Latitude', namespaces).text), 6) if stop_place.find('netex:Centroid/netex:Location/netex:Latitude', namespaces) is not None else ''
    }
    stop_places.append(stop_place_data)

    for quay in stop_place.findall('netex:quays/netex:Quay', namespaces):
        quay_data = {
            'quay_id': quay.attrib.get('id', ''),
            'wgs84_e_quay': quay.find('netex:Centroid/netex:Location/netex:Longitude', namespaces).text if quay.find('netex:Centroid/netex:Location/netex:Longitude', namespaces) is not None else '',
            'wgs84_n_quay': quay.find('netex:Centroid/netex:Location/netex:Latitude', namespaces).text if quay.find('netex:Centroid/netex:Location/netex:Latitude', namespaces) is not None else '',
            'id_fli': stop_place_data['id_fli'],
            'wgs84_epsg': data_main['wgs84_epsg']
        }
        quays.append(quay_data)

with open('data/read/flixbus.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id_fli', 'name_official', 'name_long', 'name_short', 'name_alternative', 'lang', 'wgs84_e', 'wgs84_n', 'wgs84_h', 'wgs84_epsg', 'local_e', 'local_n', 'local_h', 'local_epsg', 'station_priority', 'km_info', 'stations_metastation_hrdf', 'stations_metastation']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    for stop_place in stop_places:
        row = data_main.copy()
        row.update(stop_place)
        if row['wgs84_e']!='' and float(row['wgs84_e'])<=51 and float(row['wgs84_e'])>=-26 and float(row['wgs84_n'])<=72 and float(row['wgs84_n'])>=34:
            writer.writerow(row)

with open('data/read_quays/flixbus_quays.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id_fli', 'quay_id', 'wgs84_e_quay', 'wgs84_n_quay', 'wgs84_h_quay', 'wgs84_epsg', 'local_e_quay', 'local_n_quay', 'local_h_quay', 'local_epsg']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    for quay in quays:
        if quay['wgs84_e_quay']!='' and float(quay['wgs84_e_quay'])<=51 and float(quay['wgs84_e_quay'])>=-26 and float(quay['wgs84_n_quay'])<=72 and float(quay['wgs84_n_quay'])>=34:
            writer.writerow(quay)

print("CSV-Dateien wurden erfolgreich erstellt.")