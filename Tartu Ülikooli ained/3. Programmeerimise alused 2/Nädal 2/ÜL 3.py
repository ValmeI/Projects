def voitis_nurkademangu(bingo):
    if bingo[0][0] == 'X' \
            and bingo[0][-1] == 'X' \
            and bingo[-1][0] == 'X' \
            and bingo[-1][-1] == 'X':
        return True
    else:
        return False





matrix1 = [["X", 30, 34, 55, "X"],
           [10, 16, 40, 50, 67],
           [5, 20, 38, 48, 61],
           [4, 26, 43, 49, 70],
           ["X", 17, 33, 51, "X"]]

matrix2 =[[1, 30, 34, 55, 75],
           [10, 16, 40, 50, 67],
           [5, 20, 38, 48, 61],
           [4, 26, 43, 49, 70],
           [15, 17, 33, 51, 66]]

print(voitis_nurkademangu(matrix2))
