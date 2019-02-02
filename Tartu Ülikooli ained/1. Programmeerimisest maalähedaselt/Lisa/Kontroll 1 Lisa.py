import math

laius = int(input("Mitu küpsist on tordi laius? " ))
pikkus = int(input("Aga pikkus? "))
korruseid = int(input("Mitme korruselist torti soovid? "))
pakis = int(input("Mitu küpsist on ühes pakis? "))

print("Vaja läheb " + str(laius*pikkus*korruseid) + " küpsist")
print("seega tuleks osta " + str(math.ceil((laius*pikkus*korruseid)/pakis)) + " pakki(i) küpsiseid")