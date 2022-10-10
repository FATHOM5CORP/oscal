import csv

ids = []
smts = []
objs = []
obj_dict = {}

with open('tab-delim-800-171-raw.csv', 'r') as f:
    r_dat = csv.reader(f, delimiter='\t')
    for id, smt, obj in r_dat:
        if id != '':
            ids.append(id)
            obj_dict[id] = []
            last_valid_id = id
        if smt != '':
            smts.append(smt)
            obj_dict[id].append(smt)
        if obj != '':
            objs.append(obj)
            obj_dict[last_valid_id].append(obj)

with open("parsed.txt", "w") as f:
    f.write("\t\t\t{\n")
    f.write("\t\t\t\t\"controls\": [\n")
    for key in obj_dict:
        f.write("\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\"id\": \"" + key + "\",\n")
        f.write("\t\t\t\t\t\t\"class\": \"SP800-171\",\n")
        f.write("\t\t\t\t\t\t\"title\": \"" + obj_dict[key][0] + "\",\n")
        f.write("\t\t\t\t\t\t\"props\": [\n")
        f.write("\t\t\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\t\t\"name\": \"label\",\n")
        f.write("\t\t\t\t\t\t\t\t\"value\": \"" + key + "\"\n")
        f.write("\t\t\t\t\t\t\t},\n")
        f.write("\t\t\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\t\t\"name\": \"label\",\n")
        f.write("\t\t\t\t\t\t\t\t\"value\": \"" + key + "\",\n")
        f.write("\t\t\t\t\t\t\t\t\"class\": \"sp800-171a\"\n")
        f.write("\t\t\t\t\t\t\t},\n")
        f.write("\t\t\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\t\t\"name\": \"sort-id\",\n")
        f.write("\t\t\t\t\t\t\t\t\"value\": \"" + key + "\"\n")
        f.write("\t\t\t\t\t\t\t}\n")
        f.write("\t\t\t\t\t\t],\n")
        f.write("\t\t\t\t\t\t\"parts\": [\n")
        f.write("\t\t\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\t\t\"id\": \"" + key + "_smt\",\n")
        f.write("\t\t\t\t\t\t\t\t\"name\": \"statement\",\n")
        f.write("\t\t\t\t\t\t\t\t\"prose\": \"" + obj_dict[key][0] + "\"\n")
        f.write("\t\t\t\t\t\t\t},\n")
        f.write("\t\t\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\t\t\"id\": \"" + key + "_obj\",\n")
        f.write("\t\t\t\t\t\t\t\t\"name\": \"assessment-objective\",\n")
        f.write("\t\t\t\t\t\t\t\t\"props\": [\n")
        f.write("\t\t\t\t\t\t\t\t\t{\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\"name\": \"label\",\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\"value\": \"" + key + "\",\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\"class\": \"sp800-171a\"\n")
        f.write("\t\t\t\t\t\t\t\t\t}\n")
        f.write("\t\t\t\t\t\t\t\t],\n")
        f.write("\t\t\t\t\t\t\t\t\"parts\": [\n")
        for i in range(1, len(obj_dict[key])):
            f.write("\t\t\t\t\t\t\t\t\t{\n")
            str_list = obj_dict[key][i].split(key)
            new_str = "".join(str_list)
            obj_letter = new_str[1]
            obj_prose = new_str[4:]
            f.write("\t\t\t\t\t\t\t\t\t\t\"id\": \"" + key + "_obj." + obj_letter + "\",\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\"name\": \"assessment-objective\",\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\"props\": [\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\t{\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\t\t\"name\": \"label\",\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\t\t\"value\": \"" + key + "[" + obj_letter + "]\",\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\t\t\"class\": \"sp800-171a\"\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\t}\n")
            f.write("\t\t\t\t\t\t\t\t\t\t],\n")
            f.write("\t\t\t\t\t\t\t\t\t\t\"prose\": \"" + obj_prose + "\"\n")
            if i == len(obj_dict[key]) - 1:
                f.write("\t\t\t\t\t\t\t\t\t}\n")
            else:
                f.write("\t\t\t\t\t\t\t\t\t},\n")
        f.write("\t\t\t\t\t\t\t\t]\n")
        f.write("\t\t\t\t\t\t\t}\n")
        f.write("\t\t\t\t\t\t]\n")
        f.write("\t\t\t\t\t},\n")