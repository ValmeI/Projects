def kooslubajad(list_of_promises):
    list_era = []
    list_nr = []
    yhis_osa = {}
    '# iga erakonna lubadused eraldi '
    for x in list_of_promises:
        list_era.append(x)
    #for x in args:
        #for era in x:
           # era = list(era)
           # print(era)
            #list_era.append(era)

        '#count erakonna nr'
    for n in range(len(list_era)):
        list_nr.append(n)
        '# zip kokku ja siis dict'

    dic_era = dict(zip(list_nr, list_era))

    for k, v in dic_era.items():
        '#ristkorrutis'
        for nr in list_nr:
            '#eemaldame enda ristkorrutise tulemustest'
            if k != nr:
                võrdlus = set(dic_era[k]) & set(dic_era[nr])
                '#eemaldame set() tühjad väljad'
                if võrdlus != set():
                    '#eemaldada ristkorrutise osas tekkinud toplet kirjed'
                    if k not in yhis_osa:
                        yhis_osa[k] = võrdlus
    #print(yhis_osa)

    '# tagastaks ainult ühe rea lõpus'
    result_list = []
    list_inner = []
    juba_olemas = ''
    for k2, v2 in yhis_osa.items():
       # print(k2, v2)
        if v2 not in list_inner:
            list_inner.append(v2)
        else:
            juba_olemas = v2
    #print(juba_olemas)

    for k3, v3 in yhis_osa.items():
        if v3 == juba_olemas:
            result_list.append(k3)
    #print(result_list)

    '#juhul kui ühisosa ei ole üldse'
    if len(result_list) == 0:
        result_list = [0, 1]

    return tuple(result_list)
    #for k3, v3 in yhis_osa.items():
       # if v3 in list_inner:
            #print(k3, v3)
        #for x in range(len(yhis_osa)):
            #for y in range(len(yhis_osa[x])):
               # print(x,y)


                #if line_count == 6:
                    #line_count += 1
                    #print(k2, nr2, v2, yhis_osa[k2])
                    #return tuple([k2, nr2])

 









erakond_A = {"lastetoetusi tõsta", "pensione tõsta", "tulumaksu langetada", "kaitsekulutusi tõsta"}
erakond_B = {"muuta kõike varasemat"}
erakond_C = {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"}
erakond_D = set()
erakond_E = {"väljarännet piirata", "pensione tõsta", "õpetajate palku tõsta", "kaitsekulutusi tõsta", "alkoholiaktsiisi tõsta"}

#kooslubajad([erakond_A, erakond_C])
#kooslubajad([{'kuritegevust vähendada', 'kaotada kõik maksud', 'suurendada kõiki palkasid', 'rajada spordiväljakud igasse linna', 'kõiki toetusi suurendada', 'algatada koduloometoetus'},
             #{'edendada maaelu', 'aidata noorperesid', 'toetada pensionäre', 'vähendada suremust', 'suurendada vastsündinute arvu'}])