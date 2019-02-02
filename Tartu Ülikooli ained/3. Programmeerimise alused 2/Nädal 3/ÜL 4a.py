import random

def on_bingo_tabel_extra(bingo):
    col_ok = 0
    all_list = []
    for x in range(len(bingo)):
        for y in range(len(bingo[x])):
            #print(bingo[y][x])

            '''kontrolli if unique'''
            all_list.append(bingo[x][y])

            if 1 <= bingo[y][x] <= 15:
                col_ok += 1

            if 16 <= bingo[y][x] <= 30:
                col_ok += 1

            if 31 <= bingo[y][x] <= 45:
                col_ok += 1

            if 46 <= bingo[y][x] <= 60:
                col_ok += 1

            if 61 <= bingo[y][x] <= 75:
                col_ok += 1

    '''Kontroll kas iga column on ikka õiges vahemikus ja if unique lõpp. Setis ei tohi olla asju topelt ehk siis len oleks erineva kui midagi topelt '''
    if len(all_list) == len(set(all_list)) \
            and col_ok == 25:

        return True
    else:
        return False


def juhuslik_bingo():
    first_nr = 1
    last_nr = 16
    inner_list = []
    final_bingo_list = []
    '# create transposed list'
    for x in range(0, 5):
        row = random.sample(range(first_nr, last_nr), 5)
        inner_list.append(row)
        first_nr += 15
        last_nr += 15

    '# keerame lihtsalt eelmise maatriksi teist pidi, ehk row on col ja col on row'
    for col in range(len(inner_list)):
        '# list peab siin olema, üleval ei sobi'
        bingo_inner_list = []
        for row in range(len(inner_list[col])):
            new = inner_list[row][col]
            bingo_inner_list.append(new)
        final_bingo_list.append(bingo_inner_list)

    '# kontroll kas on nr parameetrid täidetud'
    kontroll = on_bingo_tabel_extra(final_bingo_list)

    if kontroll:
        return final_bingo_list


print(juhuslik_bingo())
