Isikukood = input("Sisesta isikudkood: ")
if Isikukood[0] in ("1", "3", "5"): #kuna isikukood in string siis peaks võrdelma ka stringi
    print("He")
elif Isikukood[0] in ("2", "4", "6"):
    print("She")