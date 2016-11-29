file_path = "22-Namelist.txt"
result_dic = {}

with open(file_path, "r") as open_file:
    name = open_file.readline()
    while name:
        name = name.strip()
        if name not in result_dic:
            result_dic[name] = 1
        else:
            result_dic[name] += 1

        name = open_file.readline()

print(result_dic)