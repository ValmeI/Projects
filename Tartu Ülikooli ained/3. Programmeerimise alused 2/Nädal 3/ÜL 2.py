input_file = input("Sisestage andmebaasi faili nimi: ")#"aasia.txt"#
piir = input("Piiriületajad: ")
piir = piir.split()

def failist_sonastik(file):

    open_list = []
    file_open = open(file, encoding="UTF-8")
    '#open file and split int to list in list'
    for row in file_open:
        open_list.append(row.split())

    '#list in list to dict'
    dict_reg = dict(open_list)

    #print(dict_reg)
    return dict_reg


def tahised_nimedeks(open_list, function_dict):
    return_list = []
    for sym in open_list:
        if sym not in function_dict:
            return_list.append(None)
        elif sym in function_dict:
            return_list.append(function_dict[sym])

    #print(return_list)
    return return_list


for x in tahised_nimedeks(piir, failist_sonastik(input_file)):
    if x is None:
        print("Tundmatu maa")
    else:
        print(x)

#tahised_nimedeks(piir, failist_sonastik(input_file))
#failist_sonastik(input_file)
