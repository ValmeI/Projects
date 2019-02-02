import random

ft_toe = int(input("Sisestage visketabavuse protsent: "))
ft_shots = 1
ft_made = 0
ft_missed = 0


while ft_shots < 1001:

    if random.randint(1, 100) <= ft_toe:
        tulemus = "tabas"
        ft_made += 1
    else:
        tulemus = "mööda"
        ft_missed += 1

    print(str(ft_shots) + ". vise", tulemus)
    ft_shots += 1

print("Tabas ", ft_made, "viset.")

