from codes.general.general import create_metastations

create_metastations(download=False, buffer=True, fuzzy=True, nearest_neighbours=True, name_start="Zürich", output="Test_001")

'''
+-------------------------+---------------------------------------------------------+
| attribute name          | explanation of the attribute                            |
+-------------------------+---------------------------------------------------------+
+---main-attributes-------+---------------------------------------------------------+
| download                | explanation: checks for new data, downloads and merges  |
|                         |              it with existing data                      |
|                         | options:     True                                       |
|                         |              False                                      |
|                         | default:     True                                       |
+-------------------------+---------------------------------------------------------+
| buffer                  | explanation: groups the stations with the buffer method |
|                         | options:     True                                       |
|                         |              False                                      |
|                         | default:     False                                      |
|                         | requires:    b_r_max                                    |
|                         |              b_r_middle                                 |
|                         |              b_r_min                                    |
|                         |              b_similarity_max                           |
|                         |              b_similarity_middle                        |
+-------------------------+---------------------------------------------------------+
| fuzzy                   | explanation: groups the stations with the fuzzy-string- |
|                         |              matching method                            |
|                         | options:     True                                       |
|                         |              False                                      |
|                         | default:     False                                      |
|                         | requires:    f_similarity_max                           |
|                         |              f_dist_max                                 |
|                         |              f_similarity_middle                        |
|                         |              f_dist_middle                              |
|                         |              f_similarity_min                           |
|                         |              f_dist_min                                 |
+-------------------------+---------------------------------------------------------+
| nearest_neighbours      | explanation: groups the stations with the nearest       |
|                         |              neighbours method                          |
|                         | options:     True                                       |
|                         |              False                                      |
|                         | default:     False                                      |
|                         | requires:    nn_max_dist                                |
|                         |              nn_direct_grouping_dist                    |
|                         |              nn_similarity                              |
+-------------------------+---------------------------------------------------------+
| name_start              | explanation: filters the data by names starting with    |
|                         |              the input string (doesn't work for nearest |
|                         |              neighbours-method)                         |
|                         | options:     any string                                 |
|                         | default:     ""                                         |
+-------------------------+---------------------------------------------------------+
| output                  | explanation: defines the name of the output NeTEx-file  |
|                         | options:     any string                                 |
|                         | default:     "output"                                   |
+-------------------------+---------------------------------------------------------+
+---buffer----------------+-optional------------------------------------------------+
| b_r_max                 | explanation: sets the maximum radius for the grouping   |
|                         |              (with name similarity)                     |
|                         |              in relation to b_similarity_max            |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     200                                        |
+-------------------------+---------------------------------------------------------+
| b_r_middle              | explanation: sets the middle radius for the grouping    |
|                         |              (with name similarity)                     |
|                         |              in relation to b_similarity_middle         |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     150                                        |
+-------------------------+---------------------------------------------------------+
| b_r_min                 | explanation: sets the minimum radius for the grouping   |
|                         |              (without name similarity)                  |
|                         | options:     any number between 0 and 1                 |
|                         | default:     50                                         |
+-------------------------+---------------------------------------------------------+
| b_similarity_max        | explanation: sets the maximum distance for the direct   |
|                         |              grouping with the nearest neighbours       |
|                         |              method                                     |
|                         |              in relation to b_r_max                     |
|                         | options:     any number between 0 and 1                 |
|                         | default:     0.6                                        |
+-------------------------+---------------------------------------------------------+
| b_similarity_middle     | explanation: sets the minimum name similarity for the   |
|                         |              nearest neighbours method                  |
|                         |              in relation to b_r_middle                  |
|                         | options:     any number between 0 and 1                 |
|                         | default:     0.5                                        |
+-------------------------+---------------------------------------------------------+
+---fuzzy-----------------+-optional------------------------------------------------+
| f_similarity_max        | explanation: sets the minimum similarity for the        |
|                         |              grouping with the maximum distance         |
|                         |              in relation to f_dist_max                  |
|                         | options:     any number between 0 and 1                 |
|                         | default:     0.6                                        |
+-------------------------+---------------------------------------------------------+
| f_dist_max              | explanation: sets the maximum distance for the grouping |
|                         |              in relation to f_similarity_max            |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     300                                        |
+-------------------------+---------------------------------------------------------+
| f_similarity_middle     | explanation: sets the minimum similarity for the        |
|                         |              grouping with the middle distance          |
|                         |              in relation to f_dist_middle               |
|                         | options:     any number between 0 and 1                 |
|                         | default:     0.4                                        |
+-------------------------+---------------------------------------------------------+
| f_dist_middle           | explanation: sets the middle distance for the grouping  |
|                         |              in relation to f_similarity_middle         |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     150                                        |
+-------------------------+---------------------------------------------------------+
| f_similarity_min        | explanation: sets the minimum similarity for the        |
|                         |              grouping with the minimum distance         |
|                         |              in relation to f_dist_min                  |
|                         | options:     any number between 0 and 1                 |
|                         | default:     0.1                                        |
+-------------------------+---------------------------------------------------------+
| f_dist_min              | explanation: sets the minimum distance for the grouping |
|                         |              in relation to f_similarity_min            |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     50                                         |
+-------------------------+---------------------------------------------------------+
+---nearest-neighbours----+-optional------------------------------------------------+
| nn_max_dist             | explanation: sets the maximum distance for the grouping |
|                         |              with name similarity                       |
|                         |              in relation to nn_similarity               |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     300                                        |
+-------------------------+---------------------------------------------------------+
| nn_direct_grouping_dist | explanation: sets the maximum distance for the direct   |
|                         |              grouping                                   |
|                         |              method                                     |
|                         |              in meters                                  |
|                         | options:     any number                                 |
|                         | default:     100                                        |
+-------------------------+---------------------------------------------------------+
| nn_similarity           | explanation: sets the minimum name similarity           |
|                         |              in relation to nn_max_dist                 |
|                         | options:     any number between 0 and 1                 |
|                         | default:     0.6                                        |
+-------------------------+---------------------------------------------------------+
'''

'''
Unfinished:
download-section (also some readers are not fully reading all necessary data yet)
saving as NeTEx is not fully functional
merging function is not ideal yet
'''