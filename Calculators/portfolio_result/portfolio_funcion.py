
def file_result_to_list(file):
    file_o = open(file, encoding="utf8")
    file_text = []
    for x in file_o:
        file_text.append(x)
    return file_text



