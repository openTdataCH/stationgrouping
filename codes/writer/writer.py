import csv
import os
from decimal import Decimal
from typing import Iterator
#from datetime import datetime
import zoneinfo

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime
#from xsdata.utils.dates import calculate_timezone

from generated import StopPlace, TopographicPlace, Quay, MultilingualString, SimplePointVersionStructure, LocationStructure2, SiteFrame, StopPlacesInFrameRelStructure, CompositeFrame, FramesRelStructure, PublicationDelivery, DataObjectsRelStructure, KeyList, KeyValueStructure, Extensions2, VersionFrameDefaultsStructure, LocaleStructure, TopographicPlacesInFrameRelStructure, TopographicPlaceDescriptorVersionedChildStructure, QuaysRelStructure

quays_dict = {}

'''
with open ("data/OeV_Sammlung_CH_HRDF_5_40_41_2024_20240110_201500_quay.csv", 'r') as quay_csvfile:
    quay_reader = csv.DictReader(quay_csvfile, delimiter=";")
    for row in quay_reader:
        #parts = row.split(";")
        row: dict
        #print(row['id_sloid_quay'])
        if row['station_id_didok'] in quays_dict:
            quays_dict['station_id_didok'] = quays_dict['station_id_didok'] + [row['id_sloid_quay']]#[Quay(
                                             #   id=row['id_sloid_quay'] if row['id_sloid_quay'] != '' else None,
                                             #   #version="any",
                                             #   key_list=KeyList(key_value=[
                                             #                       KeyValueStructure(key="SLOID", value=row['id_sloid_quay'])
                                             #                       #TODO
                                             #                       ]
                                             #                   ) if row['id_sloid_quay'] != '' else None,
                                             #   centroid=SimplePointVersionStructure(location=LocationStructure2(longitude=Decimal(row['wgs84_e_quai']), latitude=Decimal(row['wgs84_n_quai']))) if row['wgs84_e_quai'] and row['wgs84_n_quai'] != '' else None,
                                             #   #public_code=row['id_sloid_quay'].split(":")[-1] if row['id_sloid_quay'] != '' else None
                                             # )]
        else:
            quays_dict['station_id_didok'] = [row['id_sloid_quay']]#[Quay(
                                             #   id=row['id_sloid_quay'] if row['id_sloid_quay'] != '' else None,
                                             #   #version="any",
                                             #   key_list=KeyList(key_value=[
                                             #                       KeyValueStructure(key="SLOID", value=row['id_sloid_quay'])
                                             #                       #TODO
                                             #                       ]
                                             #                   ) if row['id_sloid_quay'] != '' else None,
                                             #   centroid=SimplePointVersionStructure(location=LocationStructure2(longitude=Decimal(row['wgs84_e_quai']), latitude=Decimal(row['wgs84_n_quai']))) if row['wgs84_e_quai'] and row['wgs84_n_quai'] != '' else None,
                                             #   #public_code=row['id_sloid_quay'].split(":")[-1] if row['id_sloid_quay'] != '' else None
                                             # )]
    #print(row['station_id_didok'])
print(quays_dict)
'''
#def test(input_csv_path: str):
#    with open (input_csv_path + "_quay.csv", 'r') as quay_csvfile:
#        quay_reader = csv.DictReader(quay_csvfile, delimiter=";")
#        for row in quay_reader:
#            row: dict

def transform_quays(input_csv_path: str, filter) -> Iterator[Quay]:
    with open (input_csv_path + "_quay.csv", 'r') as quay_csvfile:
        quay_reader = csv.DictReader(quay_csvfile, delimiter=";")
        for row in quay_reader:
            row: dict
            if row['station_id_didok'] == filter:
                yield Quay(
                    id=row['id_sloid_quay'] if row['id_sloid_quay'] != '' else None,
                    #version="any",
                    key_list=KeyList(key_value=[
                                        KeyValueStructure(key="SLOID", value=row['id_sloid_quay'])
                                        #TODO
                                        ]
                                    ) if row['id_sloid_quay'] != '' else None,
                    centroid=SimplePointVersionStructure(location=LocationStructure2(longitude=Decimal(row['wgs84_e_quai']), latitude=Decimal(row['wgs84_n_quai']))) if row['wgs84_e_quai'] and row['wgs84_n_quai'] != '' else None,
                    public_code=row['id_sloid_quay'].split(":")[-1] if row['id_sloid_quay'] != '' else None
                )# if row['station_id_didok'] == filter else None


#<Quay/>     -> if every attribute=None #TODO

def transform_s_p(input_csv_path: str) -> Iterator[StopPlace]:
    with open(input_csv_path + ".csv", 'r') as csvfile:
        #count = 1
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            row: dict
            yield StopPlace(
                id=row['id_sloid'] if row['id_sloid'] != '' else None,
                #version="any",
                key_list=KeyList(key_value=[
                                    KeyValueStructure(key="DIDOK", value=row['id_didok']) if row['id_didok'] != '' else None,
                                    KeyValueStructure(key="SLOID", value=row['id_sloid']) if row['id_sloid'] != '' else None
                                    #TODO
                                    ]
                                ),
                #extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaximumSpeed", text=vehicle_type.speed)]), #TODO
                name=MultilingualString(value=row['name_official']),
                private_code=row['id_didok'],
                centroid=SimplePointVersionStructure(location=LocationStructure2(longitude=Decimal(row['wgs84_e']), latitude=Decimal(row['wgs84_n']))) if row['wgs84_n'] != '' and row['wgs84_e'] != '' else None,
                #quays=QuaysRelStructure(quay_ref_or_quay=list(transform_quays(input_csv_path=input_csv_path, filter=row['id_didok'])))
            )
            #print(f"Quay {count} abgeschlossen")
            #count += 1

def transform_t_p(input_csv_path: str) -> Iterator[TopographicPlace]:
    with open(input_csv_path + ".csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            row: dict
            yield TopographicPlace(
                descriptor=TopographicPlaceDescriptorVersionedChildStructure(name=MultilingualString(value=row['name_official']))
            )

def write_NeTEx(method, output_name):
    print("---Writing data to NeTEx format")
    #site_frame = SiteFrame(id="SiteFrame", version="1", stop_places=StopPlacesInFrameRelStructure(stop_place=list(transform("data/grouped/grouped.csv"))))
    site_frame = SiteFrame(topographic_places=TopographicPlacesInFrameRelStructure(topographic_place=list(transform_t_p(f"data/grouped/grouping{method}"))) ,stop_places=StopPlacesInFrameRelStructure(stop_place=list(transform_s_p(f"data/grouped/grouping{method}"))))

    composite_frame = CompositeFrame(
                            id="CompositeFrame",
                            version="1",
                            frame_defaults=VersionFrameDefaultsStructure(default_locale=LocaleStructure(time_zone_offset=Decimal(1), summer_time_zone_offset=Decimal(2), default_language="de")),
                            frames=FramesRelStructure(choice=[site_frame])
                            )

    publication_delivery = PublicationDelivery(
        publication_timestamp=XmlDateTime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin")),
        participant_ref=None,
        #description=MultilingualString(value=None),
        data_objects=DataObjectsRelStructure(choice=[composite_frame]),
        version="1.10"
    )

    serializer_config=SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print=True
    serializer_config.ignore_default_attributes=True
    serializer=XmlSerializer(config=serializer_config)

    ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'siri': 'http://www.siri.org.uk/siri'}

    if not os.path.exists(f"output/{output_name}{method}"):
        os.mkdir(f"output/{output_name}{method}")
    new_file_path = os.path.join(f"output/{output_name}{method}/SITE.xml")
    with open(new_file_path, 'w') as out:
        serializer.write(out, publication_delivery, ns_map)
    print(f"Saved data in output/{output_name}{method}")