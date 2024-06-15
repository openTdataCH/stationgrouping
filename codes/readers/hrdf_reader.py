#---Imports----------------------------------
import os

#---Pre-variables----------------------------
dict_stations = {}
dict_metastations = {}
dict_walkingtime = {}
dict_coordinates = {}
dict_limitations = {}
dict_globalids = {}
dict_stationpriorities = {}
dict_kminfo = {}
dict_railtrack = {}
dict_railtrackinfrastructure = {}
dict_changetimerides = {}
dict_changetimestations = {}
dict_changetimelines = {}
dict_changecompany = {}
dict_company = {}
dict_companytu = {}
dict_transporttype = {}
dict_cl_opt_cat = {}
dict_lines = {}

dict_mixed = {}

#---Pre-functions----------------------------
def read_BAHNHOF(path):
    file = open(path, "r")
    dict_stations.clear()

    for line in file:
        new_dict_element = []

        line = line.strip()
        parts = line.split("$<")
        id_number, official_name = parts[0].split(maxsplit=1)

        new_dict_element.append(id_number)
        new_dict_element.append(official_name)

        new_list = []
        for part in parts[1:]:
            attr_type, attr_value = part.split(">", 1)
            new_list.append(attr_type)
            new_list.append(attr_value.strip('$'))
        new_list.pop()
        new_list.pop(0)

        count = 0
        list_numbers = []
        list_names = []
        for element in new_list:
            if count % 2 == 0 or count == 0:
                list_names.append(element)
            else:
                list_numbers.append(element)
            count += 1

        long_designation = None
        abbreviation = None
        alternative_designations = None

        count = 0
        for element in list_numbers:
            if element == "2":
                long_designation = list_names[count]
                count += 1
            elif element == "3":
                abbreviation = list_names[count]
                count += 1
            elif element == "4":
                alternative_designations = list_names[count]

        new_dict_element.append(long_designation)
        new_dict_element.append(abbreviation)
        new_dict_element.append(alternative_designations)

        dict_stations[new_dict_element[0]] = [new_dict_element[1],
                                              new_dict_element[2],
                                              new_dict_element[3],
                                              new_dict_element[4]]

    file.close()

def read_BETRIEB(path):
    filede = open(path + "_DE", "r")
    file_list = ["_EN", "_FR", "_IT"]
    for line in filede:
        parts = line.strip().split()
        if line[6] == "K":
            parts_combined = parts[6]
            for element in parts[7:]:
                parts_combined = parts_combined + " " + element
            dict_companytu[parts[0]] = [[parts[2][1:-1], parts[4][1:-1], parts_combined[1:-1]]]
            for fileending in file_list:
                file_language = open(path + fileending)
                for line_language in file_language:
                    if line_language.startswith(line[0:7]):
                        parts_language = line_language.strip().split()
                        parts_language_combined = parts_language[6]
                        for element in parts_language[7:]:
                            parts_language_combined = parts_language_combined + " " + element
                        dict_companytu[parts_language[0]].append([parts_language[2][1:-1], parts_language[4][1:-1], parts_language_combined[1:-1]])
                file_language.close()
        elif line[6] == ":":
            dict_companytu[parts[0]].append(parts[2])
            dict_companytu[parts[0]] = [dict_companytu[parts[0]][-1]] + dict_companytu[parts[0]][0:-1]
    for element in dict_companytu:
        dict_company[dict_companytu[element][0]] = [element] + dict_companytu[element][1:]
    filede.close()

def read_BFKOORD(path):
    dict_coordinates.clear()
    file = open(path + "/BFKOORD_LV95", "r")
    for line in file:
        parts = line.strip().split()
        while parts[-1] != "%":
            parts.pop()
        parts.pop()
        dict_coordinates[parts[0]] = parts
    file.close()
    file = open(path + "/BFKOORD_WGS", "r")
    for line in file:
        parts = line.strip().split()
        while parts[-1] != "%":
            parts.pop()
        parts.pop()
        all_parts = dict_coordinates[parts[0]]
        for element in parts:
            if element != parts[0]:
                all_parts.append(element)
        all_parts = [all_parts[0], [all_parts[1:4], all_parts[4:]]]
        dict_coordinates[all_parts[0]] = all_parts[1:]
    file.close()

def read_BFPRIOS(path):
    file = open(path, "r")
    for line in file:
        parts = line.strip().split()
        parts_combined = parts[2]
        for element in parts[2:]:
            parts_combined = parts_combined + " " + element
        dict_stationpriorities[parts[0]] = [parts[1]] + [parts_combined]
    file.close()

def read_BHFART_60(path):
    beschraenkungen = False
    globale_ids = False
    file = open(path, "r")
    for line in file:
        if line.startswith("% Beschränkungen"):
            beschraenkungen = True
            globale_ids = False
        elif line.startswith("% Globale IDs"):
            globale_ids = True
            beschraenkungen = False
        elif line[0].isdigit() and beschraenkungen == True:
            parts = line.strip().split()
            while parts[-1] != "%":
                parts.pop()
            parts.pop()
            dict_limitations[parts[0]] = parts[1:]
        elif line[0].isdigit() and globale_ids == True:
            parts = line.strip().split()
            if parts[2] == "A":
                dict_globalids[parts[0]] = parts[2:]
            elif parts[2] == "a":
                if parts[0] in dict_globalids:
                    dict_globalids[parts[0]] = dict_globalids[parts[0]] + [parts[2:]]
                else:
                    dict_globalids[parts[0]] = [' ', ' ', ' '] + [parts[2:]]
        else:
            beschraenkungen = False
            globale_ids = False
    file.close()

def read_GLEIS(path):
    new_dict = {}

    file = open(path + "/GLEIS_WGS", "r")
    for line in file:
        if line[8] == "#" and line[17] == "K":
            if line[0:7] in new_dict:
                new_dict[line[0:7]].append([line[8:16], [line[19:27], line[28:-1]]])
            else:
                new_dict[line[0:7]] = [[line[8:16], [line[19:27], line[28:-1]]]]
    file.close()

    file = open(path + "/GLEIS_LV95", "r")
    for line in file:
        if line[8] != "#":
            pass
            '''
            parts = [line[0:7], line[8:14], line[15:21], line[22:30]]

            if line[31] != " ":
                parts.append(line[31:35])
            else:
                parts.append(None)
            if line[36] != " ":
                parts.append(line[36:])
            else:
                parts.append(None)

            if parts[0] in dict_railtrack:
                dict_railtrack[parts[0]] = dict_railtrack[parts[0]] + [parts[1:]]
            else:
                dict_railtrack[parts[0]] = [parts[1:]]
            pass
            '''
        elif line[8] == "#":
            if line[17] == "G":
                if line[20] == "'":
                    parts = [line[0:7], line[8:16], None]
                else:
                    parts = [line[0:7], line[8:16], line[20]]
                if parts[0] in dict_railtrackinfrastructure:
                    dict_railtrackinfrastructure[parts[0]] = dict_railtrackinfrastructure[parts[0]] + [parts[1:]]
                else:
                    dict_railtrackinfrastructure[parts[0]] = [parts[1:]]
            elif line[17] == "I":
                parts = [line[0:7], line[21:-1]]
                dict_railtrackinfrastructure[parts[0]][-1].append(parts[1])
            elif line[17] == "K":
                parts = [line[0:7], [line[19:26], line[27:34]]]
                if parts[0] in new_dict:
                    for element in new_dict[parts[0]]:
                        if element[0] == line[8:16]:
                            parts.append(element[-1])
                dict_railtrackinfrastructure[parts[0]][-1].append(parts[1:])
    file.close()

def read_KMINFO(path):
    file = open(path, "r")
    for line in file:
        parts = line.strip().split()
        parts_combined = parts[2]
        for element in parts[2:]:
            parts_combined = parts_combined + " " + element
        dict_kminfo[parts[0]] = [parts[1]] + [parts_combined]
    file.close()

def read_LINIE(path):
    file = open(path, "r")
    for line in file:
        if line[8:].startswith("K") or line[8:].startswith("W") or line[8:].startswith("F") or line[8:].startswith("B") or line[8:].startswith("H"):
            parts = [line[0:7], line[8], line[10:-1]]
            if parts[0] in dict_lines:
                dict_lines[parts[0]].append(parts[1:3])
            else:
                dict_lines[parts[0]] = [parts[1:3]]
        elif line[8:].startswith("I"):                                      # Noch Beispiele mit I anschauen
            parts = [line[0:7], line[8], line[10:-1]]
            if parts[0] in dict_lines:
                dict_lines[parts[0]].append(parts[1:3])
            else:
                dict_lines[parts[0]] = [parts[1:3]]
        elif line[8:].startswith("N T") or line[8:].startswith("L T") or line[8:].startswith("D T"):
            parts = [line[0:7], line[8:11], line[12:-1]]
            if parts[0] in dict_lines:
                dict_lines[parts[0]].append(parts[1:3])
            else:
                dict_lines[parts[0]] = [parts[1:3]]
        elif line[8:].startswith("R T"):                                    # Noch Beispiele mit R T anschauen
            print("R T detected")
    file.close()

def read_METABHF(path):
    file = open(path, "r")

    dict_metastations.clear()
    dict_walkingtime.clear()

    for line in file:
        if ":" in line:
            parts = line.strip().split(":")
            key = parts[0].strip()
            values = parts[1].split()
            combined_values = [key] + values
            for val in combined_values:
                dict_metastations[key] = combined_values
        elif line[0].isdigit():
            parts = line.strip().split()
            from_station = parts[0]
            to_station = parts[1]
            distance_minutes = int(parts[2])
        elif line.startswith("*"):
            if from_station in dict_walkingtime:
                dict_walkingtime[from_station].append([to_station, distance_minutes])
            else:
                dict_walkingtime[from_station] = [[to_station, distance_minutes]]

    for key, val in dict_metastations.items():
        for element in val:
            if element in dict_metastations:
                dict_metastations[key] = dict_metastations[key] + dict_metastations[element]
                dict_metastations[key].sort()

    for key in dict_metastations:
        dict_metastations[key] = list(dict.fromkeys(dict_metastations[key]))

    file.close()

def read_UMSTEIGZ(path):
    file = open(path, "r")
    for line in file:
        if line[41:47] == "      ":
            parts = [line[0:7], line[8:14], line[15:21], line[22:28], line[29:35], line[36:39], None, line[48:-1]]
        else:
            parts = [line[0:7], line[8:14], line[15:21], line[22:28], line[29:35], line[36:39], line[41:47], line[48:-1]]
        if parts[0] in dict_changetimerides:
            dict_changetimerides[parts[0]].append(parts[1:7])
        else:
            dict_changetimerides[parts[0]] = [parts[7], parts[1:7]]
    file.close()

def read_UMSTEIGB(path):
    file = open(path, "r")
    for line in file:
        dict_changetimestations[line[0:7]] = [line[8:10], line[11:13], line[14:-1]]
    file.close()

def read_UMSTEIGL(path):
    file = open(path, "r")
    for line in file:
        parts = line.strip().split()
        if parts[9][-1] == "!":
            parts[9] = parts[9][0:3]
            garanty = ["!"]
        else:
            garanty = [None]
        if line[57:-1] != '':
            name = [line[57:-1]]
        else:
            name = [None]
        parts = parts[0:10] + garanty + name
        if parts[0] in dict_changetimelines:
            dict_changetimelines[parts[0]].append(parts[1:11])
        else:
            dict_changetimelines[parts[0]] = [parts[11], parts[1:11]]
    file.close()

def read_UMSTEIGV(path):
    file = open(path, "r")
    for line in file:
        parts = line.strip().split()
        if line[25:] == '':
            parts = parts[0:4] + [None]
        else:
            parts = parts[0:4] + [line[25:-1]]
        if parts[0] in dict_changecompany:
            dict_changecompany[parts[0]].append(parts[1:4])
        else:
            dict_changecompany[parts[0]] = [parts[4], parts[1:4]]
    file.close()

def read_ZUGART(path):
    text = False
    language = None
    file = open(path, "r")
    for line in file:
        if line.startswith("<"):
            if "text" in line:
                text = True
            else:
                language = line[1:-2]
        elif text == False:
            parts = line.strip().split()
            if len(parts) == 8:
                pass
            elif len(parts) == 7:
                parts = parts[0:6] + [None] + [parts[6]]
            dict_transporttype[parts[0]] = parts[1:8]
        elif text == True:
            parts = line.strip().split()
            parts_combined = parts[1]
            for element in parts[2:]:
                parts_combined = parts_combined + " " + element
            parts = [parts[0]] + [language, [parts_combined]]
            if parts[0] in dict_cl_opt_cat:
                dict_cl_opt_cat[parts[0]].append(parts[1:])
            else:
                dict_cl_opt_cat[parts[0]] = [parts[1:]]
    file.close()

#---Hrdf-reader------------------------------
def Hrdf_read(folder_path, new_path):
    print(f"Reading of '{folder_path}' starts")
    dict_mixed.clear()
    not_used = []
    for filename in os.listdir(folder_path):
        if filename == "BAHNHOF":
            read_BAHNHOF(folder_path + "/" + filename)
        elif filename.startswith("BETRIEB"):
            if dict_company == {}:
                read_BETRIEB(folder_path + "/BETRIEB")
            else:
                pass
        elif filename.startswith("BFKOORD_"):
            if dict_coordinates == {}:
                read_BFKOORD(folder_path)
            else:
                pass
        elif filename == "BFPRIOS":
            read_BFPRIOS(folder_path + "/" + filename)
        elif filename == "BHFART_60":
            read_BHFART_60(folder_path + "/" + filename)
        elif filename.startswith("GLEIS"):
            if dict_railtrackinfrastructure == {}:
                read_GLEIS(folder_path)
            else:
                pass
        elif filename == "LINIE":
            read_LINIE(folder_path + "/" + filename)
        elif filename == "KMINFO":
            read_KMINFO(folder_path + "/" + filename)
        elif filename == "METABHF":
            read_METABHF(folder_path + "/" + filename)
        elif filename == "UMSTEIGB":
            read_UMSTEIGB(folder_path + "/" + filename)
        elif filename == "UMSTEIGL":
            read_UMSTEIGL(folder_path + "/" + filename)
        elif filename == "UMSTEIGV":
            read_UMSTEIGV(folder_path + "/" + filename)
        elif filename == "UMSTEIGZ":
            read_UMSTEIGZ(folder_path + "/" + filename)
        elif filename == "ZUGART":
            read_ZUGART(folder_path + "/" + filename)
        else:
            not_used.append(filename)
    print("Das Lesen der Dateien ["+str(not_used)+"] wird nicht unterstützt")

    for element in dict_stations:
        if element in dict_globalids:
            dict_mixed[element] = [element] + [dict_globalids[element][1]]
        else:
            dict_mixed[element] = [element] + ['']
    for element in dict_mixed:
        if element in dict_metastations:
            dict_mixed[element] = dict_mixed[element] + dict_stations[element] + [[dict_metastations[element]]]
        else:
            dict_mixed[element] = dict_mixed[element] + dict_stations[element] + [[['']]]
        if element in dict_walkingtime:
            dict_mixed[element][-1].append(dict_walkingtime[element][-1][-1])
        else:
            dict_mixed[element][-1].append('')
        if element in dict_coordinates:
            dict_mixed[element] = dict_mixed[element] + dict_coordinates[element]
        else:
            dict_mixed[element] = dict_mixed[element] + [[['', '', ''], ['', '', '']]]

    print(f"Reading of '{folder_path}' finished")

    file_path = os.path.join("data/read", new_path + ".csv")
    with open(file_path, 'w') as csv_file:
        csv_file.write("id_didok;id_sloid;name_official;name_long;name_short;name_alternative;stations_metastation;wgs84_e;wgs84_n;wgs84_h;wgs84_epsg;local_e;local_n;local_h;local_epsg\n")
        for element in dict_mixed:
            id_didok = (dict_mixed[element][0])
            id_sloid = (dict_mixed[element][1])
            station_name_official = str(dict_mixed[element][2]) if str(dict_mixed[element][2]) != "None" else ''
            station_name_long = str(dict_mixed[element][3]) if str(dict_mixed[element][3]) != "None" else ''
            station_name_short = str(dict_mixed[element][4]) if str(dict_mixed[element][4]) != "None" else ''
            station_name_alternative = str(dict_mixed[element][5]) if str(dict_mixed[element][5]) != "None" else ''
            metastation = ""
            for station in dict_mixed[element][6][0]:
                if metastation == "":
                    metastation = metastation + str(station)
                else:
                    metastation = metastation + "," + str(station)
            station_metastation = metastation
            station_coordinates_local_e = str(dict_mixed[element][7][0][0])
            station_coordinates_local_n = str(dict_mixed[element][7][0][1])
            station_coordinates_local_h = str(dict_mixed[element][7][0][2])
            if str(dict_mixed[element][7][1][2]) != '':
                local_epsg = "EPSG:2056"
            else:
                local_epsg = ''
            station_coordinates_WGS84_e = str(dict_mixed[element][7][1][0])
            station_coordinates_WGS84_n = str(dict_mixed[element][7][1][1])
            station_coordinates_WGS84_h = str(dict_mixed[element][7][1][2])
            if str(dict_mixed[element][7][1][2]) != '':
                wgs84_epsg = "EPSG:4326"
            else:
                wgs84_epsg = ''
            csv_file.write(f"{id_didok};{id_sloid};{station_name_official};{station_name_long};{station_name_short};{station_name_alternative};{station_metastation};{station_coordinates_WGS84_e};{station_coordinates_WGS84_n};{station_coordinates_WGS84_h};{wgs84_epsg};{station_coordinates_local_e};{station_coordinates_local_n};{station_coordinates_local_h};{local_epsg}\n")
    print(f"CSV-Datei wurde erstellt: {file_path}")

    '''
    file_path = os.path.join("data/read", folder_path + "_quay.csv")
    with open(file_path, 'w') as csv_file:
        csv_file.write("station_id_didok;link_id_quay;name_quay;id_sloid_quay;wgs84_e_quai;wgs84_n_quai;wgs84_epsg_quai;local_e_quai;local_n_quai;local_epsg_quai\n")
        for station in dict_railtrackinfrastructure:
            station_id_didok = station
            for element in dict_railtrackinfrastructure[station]:
                link_id_railtrack = element[0]
                name_railtrack = element[1] if element[1] != None else ''
                if len(element)==3:
                    id_sloid_railtrack = element[2]
                    local_e_quai, local_n_quai, wgs84_e_quai, wgs84_n_quai = '', '', '', ''
                elif len(element)==4:
                    id_sloid_railtrack = element[2]
                    local_e_quai = element[3][0][0]
                    local_n_quai = element[3][0][1]
                    if len(element[3])==2:
                        wgs84_e_quai = element[3][1][0]
                        wgs84_n_quai = element[3][1][1]
                    else:
                        wgs84_e_quai = ''
                        wgs84_n_quai = ''
                else:
                    id_sloid_railtrack, local_e_quai, local_n_quai, wgs84_e_quai, wgs84_n_quai = '', '', '', '', ''
                if local_e_quai != '':
                    local_epsg_quai = "EPSG:2056"
                else:
                    local_epsg_quai = ''
                if wgs84_e_quai != '':
                    wgs84_epsg_quai = "EPSG:4326"
                else:
                    wgs84_epsg_quai = ''
                line = f"{station_id_didok};{link_id_railtrack};{name_railtrack};{id_sloid_railtrack};{wgs84_e_quai};{wgs84_n_quai};{wgs84_epsg_quai};{local_e_quai};{local_n_quai};{local_epsg_quai}"
                csv_file.write(line.strip("\n") + "\n")
    '''

#---Anmerkungen------------------------------
'''
 - Bei Testdatei mind. ein Bahnhof nicht bei BHFART_60 angegeben (Nur die Gleisen bei 1402566 vorhanden)
 -> Der Code wurde daran angepasst in der Funktion read_BHFART_60

 - Die Dateien mit den Gleisen weichen von der Beschreibung ab (z.B. I A statt g A)
'''