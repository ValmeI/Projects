vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ").upper()
tyyp = int(input("Sisestage treeningu tüüp: "))
minpulss = 0
maxpulss = 0

if sugu == 'M':
    pulss = 220 - vanus
    if tyyp == 1:
        minpulss = pulss * (50 / 100)
        maxpulss = pulss * (70 / 100)
    elif tyyp == 2:
        minpulss = pulss * (70 / 100)
        maxpulss = pulss * (80 / 100)
    elif tyyp == 3:
        minpulss = pulss * (80 / 100)
        maxpulss = pulss * (87 / 100)

elif sugu == 'N':
    pulss = 206 - (vanus * (88 / 100))
    if tyyp == 1:
        minpulss = pulss * (50 / 100)
        maxpulss = pulss * (70 / 100)
    elif tyyp == 2:
        minpulss = pulss * (70 / 100)
        maxpulss = pulss * (80 / 100)
    elif tyyp == 3:
        minpulss = pulss * (80 / 100)
        maxpulss = pulss * (87 / 100)

print("Pulsisagedus peaks olema vahemikus", round(minpulss) , "kuni", round(maxpulss))