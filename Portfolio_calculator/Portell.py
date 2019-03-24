from Portfolio_calculator import Kinnisvara, Morr, Valme
from Portfolio_calculator.Funcions import diff_months, need_new_excel_file, update_excel
from datetime import date
import time
import os
from dateutil.relativedelta import relativedelta
from termcolor import colored
from Send_Email import Send
from Portfolio_calculator.Funcions import what_path_for_file


'# tänane kuupäev arvutamaks, et mitu makset on tehtud juba'
Täna = date.today()

'#Kinnisvara objetktide print'
Kinnisvara.korterid()
PerMonthAka42 = Kinnisvara.apr_month(Kinnisvara.Korter1_Laen, 3, 15)
PerMonthAka38 = Kinnisvara.apr_month(Kinnisvara.Korter2_Laen, 3, 15)
PerMonthVilde90 = Kinnisvara.apr_month(Kinnisvara.Korter3_Laen, 2.39, 11)

print('\n' + Kinnisvara.Korter1_Nimi, "laenumakse:", PerMonthAka42, "€ + kindlustus.")
print(Kinnisvara.Korter2_Nimi, "laenumakse:", PerMonthAka38, "€ + kindlustus.")
print(Kinnisvara.Korter3_Nimi, "laenumakse:", PerMonthVilde90, "€ + kindlustus.\n")

'# how many years and months each loan is paid already'
dateAka42 = relativedelta(Täna, Valme.Vana_Aka42_63_Laen_Kuupäev)
dateAka38 = relativedelta(Täna, Valme.Vana_Aka38_20_Laen_Kuupäev)
dateVilde90 = relativedelta(Täna, Valme.Vilde90_193_Laen_Kuupäev)

print("Laenu Akadeemia 42-63 makstud:", dateAka42.years, "Years,", dateAka42.months, "Months")
print("Laenu Akadeemia 38-20 makstud:", dateAka38.years, "Years,", dateAka38.months, "Months")
print("Laenu Vilde 90-193 makstud:", dateVilde90.years, "Years,", dateVilde90.months, "Months\n")

'#makstud kuude vahe arvutus'
KuudMakstudAka42 = diff_months(Täna, Valme.Aka42_63_Laen_Kuupäev)
KuudMakstudAka38 = diff_months(Täna, Valme.Aka38_20_Laen_Kuupäev)
KuudMakstudVilde90 = diff_months(Täna, Valme.Vilde90_193_Laen_Kuupäev)

'#diffMonths annab natuke erineva tulemuse, kui aastad vs kuud'
BalanceAka42 = Kinnisvara.apr_balance(Kinnisvara.Korter1_Laen, 3, 15, KuudMakstudAka42)
BalanceAka38 = Kinnisvara.apr_balance(Kinnisvara.Korter2_Laen, 3, 15, KuudMakstudAka38)
BalanceVilde90 = Kinnisvara.apr_balance(Kinnisvara.Korter3_Laen, 2.39, 11, KuudMakstudVilde90)
print(Kinnisvara.Korter1_Nimi, "laenu jääk", BalanceAka42, "€.")
print(Kinnisvara.Korter2_Nimi, "laenu jääk", BalanceAka38, "€.")
print(Kinnisvara.Korter3_Nimi, "laenu jääk", BalanceVilde90, "€.")

print("\nLaenu kohutus kokku(ainult Akadeemia):", BalanceAka42 + BalanceAka38)
print("Laenu kohutus kokku(Kõik):", BalanceAka42 + BalanceAka38 + BalanceVilde90)

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

#TODO saata emale ja isale igakuine ülevaade
'# for combining results to send in e-mail'
Tulemus = "\nTerve portfell kokku: " + str(KoikKokku) + " €." + \
          "\nEesmärk krooni miljonär " + str(Eesmark) + " €." + \
          "\nVeel minna: " + str(Eesmark - KoikKokku) + " €." + \
          "\nMörr-i portfell: " + str(Morr.kokku) + " €. " + \
          "\nPere portfell kokku: " + str(Pere) + " €."

'#if it is friday and password file is in directory, then send e-mail'
if os.path.isfile(what_path_for_file() + r'Send_Email\synology_pass'):

    no_file = 'E-maili saatmine: Parooli faili ei ole kataloogis: ' + str(what_path_for_file())
    no_file = colored(no_file, 'red')

elif date.today().weekday() == 4:

    '# Variables are: STMP, username, password file, send from, send to, email title and email body'
    Send.send_email('valme.noip.me',
                    'email',
                    str(what_path_for_file()) + r'Send_Email\synology_pass',
                    'email@valme.noip.me',
                    'margit1986@gmail.com',
                    'Portfelli seis: ' + time.strftime('%d-%m-%Y'),
                    Tulemus)
else:
    print(colored('E-maili saatmine: Pole reede', 'green'))
