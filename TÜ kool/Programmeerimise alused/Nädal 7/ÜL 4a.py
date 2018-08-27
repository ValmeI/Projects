sisesta = input("Sisesta failinimi: ")
f_open = open(sisesta, encoding="UTF-8")

kutsutud = 0
tuleb = 0

for r in f_open:
    kutsutud += 1
    if r[0:1] == "+":
        tuleb += 1
    elif r[0:1] == "?":
        tuleb += 0


def eelarve(osaljad):
    ruum = osaljad * 10
    ruum += 55

    return ruum

print(tuleb, "inimest tuleb")
print("Kutstud on", kutsutud, "inimest")
print("Maksimaalne eelarve:", eelarve(kutsutud))
print("Mininmaalne eelarve:", eelarve(tuleb))