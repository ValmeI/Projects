max_list = []

def vahimatest_suurim(list):

    length = len(list)
    for r in range(0, length):
        min_row = min(list[r])
        max_list.append(min_row)
        print(max_list)

    return max(max_list)




#vahimatest_suurim(maatriks)