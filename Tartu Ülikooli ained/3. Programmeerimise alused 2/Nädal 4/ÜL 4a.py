def on_alglopuline(sisend):
    if len(sisend) > 1:
        if sisend[0] > sisend[-1]:
            return 1
        else:
            return 0
    else:
        return 0


jarjend_ruudus = [[4, 3, 2], [-1, 0]]

alglopulisi = 0
for rida in jarjend_ruudus:
    alglopulisi += on_alglopuline(rida)

print("Alglõpulisi ridu on " + str(alglopulisi))