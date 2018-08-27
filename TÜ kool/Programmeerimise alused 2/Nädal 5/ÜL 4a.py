def on_rahulik(arvamus1, arvamus2, erinevus):

    print("arvamus1=", arvamus1, "arvamus2=", arvamus2, "absoluut=", abs(arvamus1 - arvamus2), "korrutis",arvamus1 * arvamus2)
    if arvamus1 * arvamus2 == 0:
        #print("rahulik")
        return True
    elif abs(arvamus1 - arvamus2) <= erinevus:
        #print("rahulik")
        return True
    elif arvamus1 * arvamus2 > 0:
        #print("rahulik")
        return True
    else:
        return False



def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0
    for i in range(len(arvamused)):
        if len(arvamused) > i+1:
            #print(arvamused[i], arvamused[i+1], lubatud_erinevus)
            #print(on_rahulik(arvamused[i], arvamused[i + 1], lubatud_erinevus))
            if not on_rahulik(arvamused[i], arvamused[i + 1], lubatud_erinevus):
                dissonantsid += 1

    return dissonantsid

#proov = dissonantside_arv([8, -8, 5], 6)
#print(proov)

