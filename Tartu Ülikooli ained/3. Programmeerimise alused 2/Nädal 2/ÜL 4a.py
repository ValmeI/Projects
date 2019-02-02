fail = input("Sisestage failinimi: ") #"korrektne.txt"#
o_fail = open(fail, encoding="utf-8")

matrix = []

'''loome sisse loetud failist vajaliku maatriksi'''
for x in o_fail:
    x = x.split()
    matrix.append(x)

'#kontrollib rida'
def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
             #Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):

                return False
    return True


'#kontroll kas list vs set ehk siis midagi pole topelt listis'
def list_vs_set(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False

'#kontrollib veergu ehk transpondib selle reaks'
def veerg(maatriks):

    '#transpose originaal maatriks'
    transposed_matrix = []

    '#transposed list: tagastab false kui, list ei võrdu set'
    for r in range(len(maatriks)):
        inner = []
        for c in range(len(maatriks)):
            transpose = maatriks[c][r]
            '#peab olema int kuna sorted on muidu string ja range on int ja ei võrdu'
            inner.append(int(transpose))

            if len(inner) == 9:
                kontroll = list_vs_set(inner)
                if sorted(inner) != list(range(1, 10)):
                    return False

                return kontroll


def rida(maatriks):

    '#originaal: tagastab false kui, list ei võrdu set'
    for r2 in range(len(maatriks)):
        inner2 = []
        for c2 in range(len(maatriks)):
            '#peab olema int kuna sorted on muidu string ja range on int ja ei võrdu'
            inner2.append(int(maatriks[r2][c2]))

            if len(inner2) == 9:
                kontroll = list_vs_set(inner2)

                if sorted(inner2) != list(range(1, 10)):
                    return False

                return kontroll


def kogu_kontroll(maatriks):
    if kastid_korras(maatriks) and veerg(maatriks) and rida(maatriks):
        return "OK"
    else:
        return "VIGA"




#print(kastid_korras(matrix))
#print(veerg(matrix))
#print(rida(matrix))
print(kogu_kontroll(matrix))


''' õige
['3', '2', '7', '4', '8', '1', '6', '5', '9']
['1', '8', '9', '3', '6', '5', '7', '2', '4']
['6', '5', '4', '2', '7', '9', '8', '1', '3']
['7', '9', '8', '1', '3', '2', '5', '4', '6']
['5', '6', '3', '9', '4', '7', '2', '8', '1']
['2', '4', '1', '6', '5', '8', '3', '9', '7']
['8', '1', '2', '7', '9', '3', '4', '6', '5']
['4', '7', '5', '8', '1', '6', '9', '3', '2']
['9', '3', '6', '5', '2', '4', '1', '7', '8']
'''

'''' transposed
['3', '1', '6', '7', '5', '2', '8', '4', '9']
['2', '8', '5', '9', '6', '4', '1', '7', '3']
['7', '9', '4', '8', '3', '1', '2', '5', '6']
['4', '3', '2', '1', '9', '6', '7', '8', '5']
['8', '6', '7', '3', '4', '5', '9', '1', '2']
['1', '5', '9', '2', '7', '8', '3', '6', '4']
['6', '7', '8', '5', '2', '3', '4', '9', '1']
['5', '2', '1', '4', '8', '9', '6', '3', '7']
['9', '4', '3', '6', '1', '7', '5', '2', '8']
'''
