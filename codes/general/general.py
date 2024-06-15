import os
from codes.download.download import download_data
from codes.readers.hrdf_reader import Hrdf_read
from codes.readers.gtfs_reader import read_gtfs
from codes.delete.delete import delete_files_in_directory
from codes.merging.merging import merge_data
from codes.grouping_methods.grouping_buffer import grouping_buffer as gr_b
from codes.grouping_methods.grouping_fuzzy_string_matching import grouping_fuzzy as gr_f
from codes.grouping_methods.grouping_nearest_neighbours import grouping_nearest_neighbours as gr_nn
from codes.writer.writer import write_NeTEx

def create_metastations(download=True, buffer=False, fuzzy=False, nearest_neighbours=False, name_start="", output="output",
                        b_r_max=200, b_r_middle=150, b_r_min=50, b_similarity_max=0.6, b_similarity_middle=0.5,
                        f_similarity_max=0.6, f_dist_max=300, f_similarity_middle=0.4, f_dist_middle=150,
                        f_similarity_min=0.1, f_dist_min=50, nn_max_dist=300, nn_direct_grouping_dist=100, nn_similarity=0.6):
    if nearest_neighbours == False and buffer == False and fuzzy == False:
        raise ValueError("One of nearest_neighbor, buffer or fuzzy must be true")
    if download == True:
        print("---starting download")
        download_data('https://opentransportdata.swiss/de/dataset/timetable-54-2024-hrdf', 'data/downloaded/OeV_Sammlung_CH_HRDF_5')
        for entry in os.listdir('data/downloaded/OeV_Sammlung_CH_HRDF_5'):
            Hrdf_read('data/downloaded/OeV_Sammlung_CH_HRDF_5/' + entry, entry)
        delete_files_in_directory('data/downloaded/OeV_Sammlung_CH_HRDF_5')
        #download_data('https://opentransportdata.swiss/de/dataset/timetable-54-2024-hrdf', 'data/downloaded/Auvergne-Rhone-Alpes')
        #for entry in os.listdir('data/downloaded/Auvergne-Rhone-Alpes'):
        #    read_gtfs('data/downloaded/Auvergne-Rhone-Alpes/' + entry, entry)
        #delete_files_in_directory('data/downloaded/Auvergne-Rhone-Alpes')
        merge_data()
    if buffer == True:
        gr_b(buffer_1_r_m=b_r_max, buffer_2_r_m=b_r_middle, buffer_3_r_m=b_r_min, similarity_1=b_similarity_max, similarity_2=b_similarity_middle, name_start=name_start)
        write_NeTEx(method="_buffer", output_name=output)
    if fuzzy == True:
        gr_f(similarity_dist_max=f_similarity_max, dist_max=f_dist_max, similarity_dist_middle=f_similarity_middle, dist_middle=f_dist_middle, similarity_dist_min=f_similarity_min, dist_min=f_dist_min, name_start=name_start)
        write_NeTEx(method="_fuzzy", output_name=output)
    if nearest_neighbours == True:
        gr_nn(similarity_distance_threshold_m=nn_max_dist, distance_threshold_m=nn_direct_grouping_dist, similarity_threshold=nn_similarity)
        write_NeTEx(method="_nearest_neighbours", output_name=output)