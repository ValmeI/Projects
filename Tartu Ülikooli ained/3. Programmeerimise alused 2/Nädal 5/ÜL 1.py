algne = []


def alla_ules(x):
    pikkus = 0
    y = int(1)
    p6ohi = 0
    x = int(x)
    if x % 2 == 1:
        if x >= 1:
            algne.append(x)
            print(x)
            alla_ules(x-2)
        elif x <= 0 and p6ohi == 0:
            print("Põhi!")
            p6ohi += 1
            x = 0
            algne.append(x)

    while p6ohi == 1 and pikkus < len(algne):
        for pos in reversed(algne):
            pos -= 1
            if pos % 2 == 0:
                print(pos)
            pikkus += 2

    if x % 2 == 0:
        if x >= 1:
            algne.append(x)
            print(x)
            alla_ules(x - 2)
        elif x <= 0 and p6ohi == 0:
            print("Põhi!")
            p6ohi += 1
    while p6ohi == 1 and pikkus < len(algne):
        for pos in reversed(algne):
            pos -= 1
            if pos % 2 == 1:
                print(pos)
            pikkus += 2
