import os
from hrdf_reader import Hrdf_read
from gtfs_reader import read_gtfs

#dict_mixed = {}

Hrdf_read("OeV_Sammlung_CH_HRDF_5_40_41_2024_20240110_201500")
read_gtfs("DAT_AURA_GTFS_ExportAOM")

#print(dict_mixed["station_id"])