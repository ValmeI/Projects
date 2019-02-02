

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



'''

matrix1 = [[1, 30, 34, 55, 75], [10, 16, 40, 50, 67], [5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]]

matrix2 =[[1, 30, 34, 55, 76],
         [10, 16, 40, 50, 67],
         [5, 20, 38, 48, 61],
         [4, 26, 43, 49, 70],
         [15, 17, 33, 51, 66]]

print(on_bingo_tabel_extra(matrix1))
'''