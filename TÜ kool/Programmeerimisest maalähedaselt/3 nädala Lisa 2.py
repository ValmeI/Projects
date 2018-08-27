import re

autoNr = input("Sisesta number: ").upper()

if re.match("^[0-9]{3}[A-Z]{3}$", autoNr):
    print("On Eesti registreerimisnumber")
else:
    print("Ei ole Eesti registreerimisnumber")