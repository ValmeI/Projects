from Portfelli_package import Kinnisvara, Funcions, Morr, Valme
from datetime import date
from dateutil.relativedelta import relativedelta
from termcolor import colored


'# tänane kuupäev arvutamaks, et mitu makset on tehtud juba'
Täna = date.today()

'#Kinnisvara objetktide print'
Kinnisvara.korterid()
PerMonthAka42 = Kinnisvara.apr_month(Kinnisvara.Korter1_Laen, 2.75, 15)
PerMonthAka38 = Kinnisvara.apr_month(Kinnisvara.Korter2_Laen, 3.7, 15)

print(Kinnisvara.Korter1_Nimi, "laenumakse:", PerMonthAka42, "€.")
print(Kinnisvara.Korter2_Nimi, "laenumakse:", PerMonthAka38, "€.")

'#makstud kuude vahe arvutus'
KuudMakstudAka42 = Funcions.diff_months(Täna, Valme.Aka42_63_Laen_Kuupäev)
KuudMakstudAka38 = Funcions.diff_months(Täna, Valme.Aka38_20_Laen_Kuupäev)

'# how many years and months each loan is paid already'
dateAka42 = relativedelta(Täna, Valme.Aka42_63_Laen_Kuupäev)
dateAka38 = relativedelta(Täna, Valme.Aka38_20_Laen_Kuupäev)
print("\nLaenu Akadeemia 42-63 makstud:", dateAka42.years, "Years,", dateAka42.months, "Months")
print("Laenu Akadeemia 38-20 makstud:", dateAka38.years, "Years,", dateAka38.months, "Months\n")

'#diffMonths annab natuke erineva tulemuse, kui aastad vs kuud, ei tea miks, sp ka -1'
BalanceAka42 = Kinnisvara.apr_balance(Kinnisvara.Korter1_Laen, 2.75, 15, KuudMakstudAka42-1)
BalanceAka38 = Kinnisvara.apr_balance(Kinnisvara.Korter2_Laen, 3.7, 15, KuudMakstudAka38)
print(Kinnisvara.Korter1_Nimi, "laenu jääk", BalanceAka42, "€.")
print(Kinnisvara.Korter2_Nimi, "laenu jääk", BalanceAka38, "€.")

print("\nLaenu kohutus kokku:", BalanceAka42 + BalanceAka38)

'#Kinnisvara kokku. Liidetakse kõik Dics korterite ostu hinnad - balancid ehk palju laenu veel maksta'
KinnisVaraPort = Kinnisvara.KinnisvaraVaartus() - BalanceAka42 - BalanceAka38

print("\nHetkel korterite puhas väärtus kokku:", KinnisVaraPort, "€.")
KoikKokku = Valme.FysIsik + Valme.JurIsik + KinnisVaraPort

'#Ehk 1 000 000 Eesti krooni'
Eesmark = round(1000000/15.6466)

print("Juriidilise isiku väärtus:", Valme.JurIsik, "€.")
print("Füüsilise isiku aktsia portfell:", Valme.FysIsik, "€.")
print("Aktsiad/Raha Jur ja Füs isikud kokku:", Valme.FysIsik + Valme.JurIsik, "€.")
print("Terve portfell kokku:", colored(KoikKokku, 'red'), "€.")
print("Eesmärk krooni miljonär", Eesmark, "€.")
print("Veel minna", colored(Eesmark - KoikKokku, 'red'))
print("Mörr-i portfell:", colored(Morr.kokku, 'red'), "€.")
Pere = KoikKokku + Morr.kokku
print("Pere portfell kokku:", colored(Pere, 'red'), "€.")

Aktsiad_kokku = Valme.FysIsik+Valme.JurIsik

Funcions.need_new_excel_file("Portfell")

'#exceli_nimi, kinnisvara_puhas, füs_aktsiad, jur_aktsiad, aktsiad_kokku, kokku_portfell, pere portfell'
Funcions.update_excel("Portfell", KinnisVaraPort, Valme.FysIsik, Valme.JurIsik, Aktsiad_kokku, KoikKokku, Pere)

