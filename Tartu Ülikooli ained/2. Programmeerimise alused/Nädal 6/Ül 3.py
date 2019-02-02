kutsutud = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest tuleb? "))


def eelarve(osaljad):
    ruum = osaljad * 10
    ruum += 55

    return ruum

print("Maksimaalne eelarve:", eelarve(kutsutud))
print("Mininmaalne eelarve:", eelarve(tuleb))







