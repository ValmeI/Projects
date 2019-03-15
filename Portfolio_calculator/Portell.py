from Portfolio_calculator import Kinnisvara, Morr, Valme
from Portfolio_calculator.FileWriter import write_to_file, empty_file
from Portfolio_calculator.Funcions import diff_months, need_new_excel_file, update_excel
from datetime import date
from dateutil.relativedelta import relativedelta
from termcolor import colored

file_name = "Results"

'# tänane kuupäev arvutamaks, et mitu makset on tehtud juba'
Täna = date.today()

'#Kinnisvara objetktide print'
Kinnisvara.korterid()
PerMonthAka42 = Kinnisvara.apr_month(Kinnisvara.Korter1_Laen, 3, 15)
PerMonthAka38 = Kinnisvara.apr_month(Kinnisvara.Korter2_Laen, 3, 15)

print(Kinnisvara.Korter1_Nimi, "laenumakse:", PerMonthAka42, "€.")
print(Kinnisvara.Korter2_Nimi, "laenumakse:", PerMonthAka38, "€.")

'# how many years and months each loan is paid already'
dateAka42 = relativedelta(Täna, Valme.Vana_Aka42_63_Laen_Kuupäev)
dateAka38 = relativedelta(Täna, Valme.Vana_Aka38_20_Laen_Kuupäev)
print("\nLaenu Akadeemia 42-63 makstud:", dateAka42.years, "Years,", dateAka42.months, "Months")
print("Laenu Akadeemia 38-20 makstud:", dateAka38.years, "Years,", dateAka38.months, "Months\n")

'#makstud kuude vahe arvutus'
KuudMakstudAka42 = diff_months(Täna, Valme.Aka42_63_Laen_Kuupäev)
KuudMakstudAka38 = diff_months(Täna, Valme.Aka38_20_Laen_Kuupäev)

'#diffMonths annab natuke erineva tulemuse, kui aastad vs kuud'
BalanceAka42 = Kinnisvara.apr_balance(Kinnisvara.Korter1_Laen, 3, 15, KuudMakstudAka42)
BalanceAka38 = Kinnisvara.apr_balance(Kinnisvara.Korter2_Laen, 3, 15, KuudMakstudAka38)
print(Kinnisvara.Korter1_Nimi, "laenu jääk", BalanceAka42, "€.")
print(Kinnisvara.Korter2_Nimi, "laenu jääk", BalanceAka38, "€.")

print("\nLaenu kohutus kokku:", BalanceAka42 + BalanceAka38)

'#Kinnisvara kokku. Liidetakse kõik Dics korterite ostu hinnad - balancid ehk palju laenu veel maksta'
KinnisVaraPort = Kinnisvara.kinnisvara_vaartus() - BalanceAka42 - BalanceAka38

print("\nHetkel korterite puhas väärtus kokku:", KinnisVaraPort, "€.")
KoikKokku = Valme.FysIsik + Valme.JurIsik + KinnisVaraPort

'#Ehk 1 000 000 Eesti krooni'
Eesmark = round(1000000/15.6466)

print("Juriidilise isiku väärtus:", Valme.JurIsik, "€.")
print("Füüsilise isiku aktsia portfell:", Valme.FysIsik, "€.")
print("Aktsiad/Raha Jur ja Füs isikud kokku:", Valme.FysIsik + Valme.JurIsik, "€.")
print("Terve portfell kokku:", colored(KoikKokku, 'red'), "€.")
print("Eesmärk krooni miljonär", Eesmark, "€.")
print("Veel minna:", colored(Eesmark - KoikKokku, 'red'), "€.")
print("Mörr-i portfell:", colored(Morr.kokku, 'red'), "€.")
Pere = KoikKokku + Morr.kokku
print("Pere portfell kokku:", colored(Pere, 'red'), "€.")

Aktsiad_kokku = Valme.FysIsik+Valme.JurIsik

need_new_excel_file("Portfell")

'#exceli_nimi, kinnisvara_puhas, füs_aktsiad, jur_aktsiad, aktsiad_kokku, kokku_portfell, pere portfell'
update_excel("Portfell", KinnisVaraPort, Valme.FysIsik, Valme.JurIsik, Aktsiad_kokku, KoikKokku, Morr.kokku, Pere)
'# Empty a file'
empty_file(file_name)
'# Write to file'
write_to_file(file_name,
                "\nTerve portfell kokku: " + str(KoikKokku) + " €.",
                "\nEesmärk krooni miljonär " + str(Eesmark) + " €.",
                "\nVeel minna: " + str(Eesmark - KoikKokku) + " €.",
                "\nMörr-i portfell: " + str(Morr.kokku) + " €.",
                "\nPere portfell kokku: " + str(Pere) + " €.",
              )
