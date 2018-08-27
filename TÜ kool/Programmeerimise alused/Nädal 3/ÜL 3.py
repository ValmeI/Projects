from random import randint

tarv_arv = int(input("Täringute arv: "))
palju = 0

while palju < tarv_arv:
        palju += 1
        print(randint(1, 6))
