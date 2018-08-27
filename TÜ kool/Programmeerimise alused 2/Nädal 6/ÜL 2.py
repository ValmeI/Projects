def seosta_lapsed_ja_vanemad (laste_seosed_fail, nimed_fail):
    f1_open = open(laste_seosed_fail, encoding="utf-8")
    f2_open = open(nimed_fail, encoding="utf-8")

    seosed_list = []
    nimed_list = []

    '# seoste pars'
    for seos in f1_open:
        seos = seos.split()
        seosed_list.append(seos)
    #print(seosed_list)

    '# IK ja nimede pars'
    for nimed in f2_open:
        nimed = nimed.split(" ", 1)
        #print(nimed)
        nimed_list.append(nimed)
    #print(nimed_list)

    '# nimede nextline eemaldamine'
    temp_outer = []
    for x in range(len(nimed_list)):
        temp = []
        for y in range(len(nimed_list[x])):
            #print(nimed_list[x][y])
            if '\n' in nimed_list[x][y]:
                nimed_list[x][y] = nimed_list[x][y].replace('\n', '')
                #print(nimed_list[x][y])
                temp.append(nimed_list[x][y])
            else:
                #print(nimed_list[x][y])
                temp.append(nimed_list[x][y])

        temp_outer.append(temp)
    #print(temp_outer)

    dic_nimed_IK = dict(temp_outer)
    #print(seosed_list)
    #print(dic_nimed_IK)

    outer = []
    for seosIK in seosed_list:
        seos_nimed = []
        for IK in seosIK:
            nimi = dic_nimed_IK[IK]
            #print(IK, nimi)
            seos_nimed.append(nimi)
        #print(seos_nimed)
        outer.append(seos_nimed)
    #print(outer)


    temp = {}
    for x in range(len(outer)):
        li = []
        for y in range(len(outer)):
            #print(outer[x][0], outer[x][1])
            if outer[x][0] not in temp:
                temp[outer[x][0]] = set([outer[x][1]])
            #print(temp)
            else:
                pr = temp[outer[x][0]]
                pr.add(outer[x][1])

                #print(outer[x][0], pr)
                temp[outer[x][0]] = pr
    #print(temp)
    return temp

#seosta_lapsed_ja_vanemad("laste.txt", "nimed.txt")


'''
47853062345 60907062342
46906183451 38504014543
34105139833 36512129874
36512129874 38504014543
46906183451 48708252344
36512129874 48708252344

['47853062345', 'Kadri Kalkun']
['36512129874', 'Peeter Peedumets']
['38504014543', 'Maria Peedumets']
['46906183451', 'Madli Peedumets']
['34105139833', 'Karl Peedumets']
['48708252344', 'Robert Peedumets']
['60907062342', 'Liisa Maria Jaaniste']

'''

