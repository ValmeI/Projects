
def laeva_teekond(kiirus_sõlmedes):

    teekondKM = kiirus_sõlmedes * 1852 / 1000 * 24

    return round(teekondKM)



Kiirus = int(input("Mitu sõlme on laeva kiirus? "))
print("Laev läbib ööpäevas kilomeetrites:", laeva_teekond(Kiirus))