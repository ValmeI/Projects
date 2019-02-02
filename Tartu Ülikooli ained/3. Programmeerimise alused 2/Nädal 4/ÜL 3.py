def absoluutne_tabel(sisend):
    out_list = []
    for x in sisend:
        inner_list = []
        for y in x:
            if y >= 0:
                y = y
            else:
                y = y * -1
            inner_list.append(y)
        out_list.append(inner_list)
    return out_list


def absolutiseeri_tabel(sisend):
    outer_list = []
    for x in range(len(sisend)):
        inner_list = []
        for y in range(len(sisend[x])):
            if sisend[x][y] >= 0:
                sisend[x][y] = sisend[x][y]
            else:
                sisend[x][y] = sisend[x][y] * -1
            inner_list.append(sisend[x][y])
        outer_list.append(inner_list)
