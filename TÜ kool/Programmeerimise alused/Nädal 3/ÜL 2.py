ostjate_arv = int(input("Sisestage ostjate arv: "))
kokku = 0

while ostjate_arv < 0:
    ostjate_arv = int(input("Sisestage ostjate arv: "))

if ostjate_arv % 2 == 1:
    ostjate_arv = ostjate_arv
elif ostjate_arv % 2 == 0:
    ostjate_arv -= 1


while ostjate_arv > 0:
        kokku += ostjate_arv
        ostjate_arv -= 2

print(kokku)
