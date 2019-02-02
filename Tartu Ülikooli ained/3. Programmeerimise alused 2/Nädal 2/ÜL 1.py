faili_nimi = "arvud.txt"#input("Sisestage  failinimi: ")

f_open = open(faili_nimi, encoding="utf-8")

matrix = []

for r in f_open:
    r = r.split()
    matrix.append(r)

sum_matrix = []

for l in matrix:
    '''#convesrt to int in lis to sum'''
    row_sum = sum(int(i) for i in l)
    sum_matrix.append(row_sum)

mitmes_rida = 0

for k in sum_matrix:
    if k == max(sum_matrix):
        break
    else:
        mitmes_rida += 1


'''Peab +1 olema kuna muidu on count 0'ist'''
loetav_rida = mitmes_rida+1


print("Suurim summa on failis", str(loetav_rida) + ". real ja see on", max(sum_matrix))


