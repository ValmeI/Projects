from datetime import datetime
kuupäev_kellaeg = datetime.today()
sissekanne = input("Sisesta sissekande tekst: ")

a_fail = open("paevik.txt", "a", encoding="UTF-8")

a_fail.write(str(kuupäev_kellaeg) + "\n")
a_fail.write(sissekanne + "\n")

a_fail.close()
