from easygui import *

arv1 = integerbox("Sisstage esimene täisarve lõigus 1-10:", lowerbound=0, upperbound=10)
arv2 = integerbox("Sisstage teine täisarve lõigus 1-10:", lowerbound=0, upperbound=10)

nupud = ["+", "-", "*"]
vajutati = buttonbox("Valige tehe: ", choices=nupud)

if vajutati == "+":
    tulemus = arv1 + arv2
    msgbox("Tehte tulemus on " + str(tulemus))
elif vajutati == "-":
    tulemus = arv1 - arv2
    msgbox("Tehte tulemus on " + str(tulemus))
elif vajutati == "*":
    tulemus = arv1 * arv2
    msgbox("Tehte tulemus on " + str(tulemus))