def write_to_file(file_name, *args):
    '# write every row to new line (a)'
    with open(file_name + ".txt", 'a') as f:
        for x in args:
            f.write(x)


def empty_file(file_name):
    '# emptyh a file. Open and close'
    with open(file_name + ".txt", 'w') as f:
        f.close()
