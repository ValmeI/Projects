kordus = int(input("Mitu korda soovite reklaamlauset kuvada? "))
lause = input("Sisestage reklaamlause: ")



def banner(sisend_lause):
    sisend_lause = sisend_lause.upper()
    return sisend_lause



i = 0
while i < kordus:
    print(banner(lause))
    i += 1



