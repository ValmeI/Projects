kokku = []


def paarissumma(x):
    if x >= 0:
        if x % 2 == 0:
            kokku.append(x)
            paarissumma(x - 1)

        elif x % 2 == 1:
            paarissumma(x-1)

    if x == 0:
        sum(kokku)
    return sum(kokku)
