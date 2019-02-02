def kuup(jarj):
    if len(jarj) == 0:
        return jarj
    return [jarj[0] ** 3] + kuup(jarj[1:])




#[27, 125, -8]