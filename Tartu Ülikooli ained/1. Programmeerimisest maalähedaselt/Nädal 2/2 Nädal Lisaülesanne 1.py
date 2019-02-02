Töötunnid = int(input("Sisesta töötundide arve nädalas: "))
TunniTasu = int(input("Sisesta töötunni tasu: "))

if Töötunnid <= 40:
    Palk = Töötunnid*TunniTasu
    print("Nädalapalk on " + str(Palk))

elif Töötunnid > 40:
    Palk = 40 * TunniTasu + (Töötunnid-40) * (TunniTasu*1.5)
    print("Nädalapalk on " + str(Palk))