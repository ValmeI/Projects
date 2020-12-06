from Portfolio_calculator import Kinnisvara, Morr, Valme, txt_write_move
from Portfolio_calculator.Funcions import diff_months, need_new_excel_file, update_excel
from datetime import date
import datetime
import time
import os
import sys
from dateutil.relativedelta import relativedelta
from termcolor import colored
from Send_Email import Send
from Portfolio_calculator.Funcions import what_path_for_file
from shutil import copy

path = what_path_for_file()

'copy to nas webserver'
txt_source = path + r'Portfolio_calculator\Print_result.txt'
excel_source = path + r'Portfolio_calculator\Portfell.xls'
pc_des_path = path + r'Calculators\portfolio_result'
nas_des_path = r'\\RMI_NAS\Python\Calculators\portfolio_result'

'# Copy txt result and excel file to Nas server, if all the files or path exists'
if os.path.isfile(txt_source) and os.path.isfile(excel_source) and os.path.isdir(nas_des_path):
    '# Copy previously created file to Calculators directory'
    copy(txt_source, nas_des_path)
    copy(excel_source, nas_des_path)
    print("Kopeeritud edukalt")
else:
    print("Ei kopeeritud")
    pass

'# create file from consol output'
sys.stdout = txt_write_move.Logger()

'# tänane kuupäev arvutamaks, et mitu makset on tehtud juba'
Täna = date.today()
print(datetime.datetime.now())
'#Kinnisvara objetktide print'

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
dateSõle = relativedelta(Täna, Morr.Sõle_Laen_Kuupäev)

print("Laenu Akadeemia 42-63 makstud:", dateAka42.years, "Years,", dateAka42.months, "Months")
print("Laenu Akadeemia 38-20 makstud:", dateAka38.years, "Years,", dateAka38.months, "Months")
print("Laenu Vilde 90-193 makstud:", dateVilde90.years, "Years,", dateVilde90.months, "Months")
print("Laenu Sõle 25B/3-21 makstud:", dateSõle.years, "Years,", dateSõle.months, "Months\n")

'#makstud kuude vahe arvutus'
KuudMakstudAka42 = diff_months(Täna, Valme.Aka42_63_Laen_Kuupäev)
KuudMakstudAka38 = diff_months(Täna, Valme.Aka38_20_Laen_Kuupäev)
KuudMakstudVilde90 = diff_months(Täna, Valme.Vilde90_193_Laen_Kuupäev)
KuudMakstudSõle = diff_months(Täna, Morr.Sõle_Laen_Kuupäev)

'#diffMonths annab natuke erineva tulemuse, kui aastad vs kuud'
BalanceAka42 = Kinnisvara.apr_balance(Kinnisvara.Korter1_Laen, 3, 15, KuudMakstudAka42)
BalanceAka38 = Kinnisvara.apr_balance(Kinnisvara.Korter2_Laen, 3, 15, KuudMakstudAka38)
BalanceVilde90 = Kinnisvara.apr_balance(Kinnisvara.Korter3_Laen, 2.39, 11, KuudMakstudVilde90)
BalanceSõle = Kinnisvara.apr_balance(Kinnisvara.Korter4_Laen, 1.17, 30, KuudMakstudSõle)

print(Kinnisvara.Korter1_Nimi, "laenu jääk", BalanceAka42, "€.", 'Laenu summa', Kinnisvara.Korter1_Laen)
print(Kinnisvara.Korter2_Nimi, "laenu jääk", BalanceAka38, "€.", 'Laenu summa', Kinnisvara.Korter2_Laen)
print(Kinnisvara.Korter3_Nimi, "laenu jääk", BalanceVilde90, "€.", 'Laenu summa', Kinnisvara.Korter3_Laen)
print(Kinnisvara.Korter4_Nimi, "laenu jääk", BalanceSõle, "€.", 'Laenu summa', Kinnisvara.Korter4_Laen)

print("\nLaenu kohutus kokku(ainult Akadeemia):", BalanceAka42 + BalanceAka38)
print("Laenu kohutus kokku(Kõik):", BalanceAka42 + BalanceAka38 + BalanceVilde90)

'#Kinnisvara kokku. Liidetakse kõik Dics korterite ostu hinnad - balancid ehk palju laenu veel maksta'
KinnisVaraPort = Kinnisvara.kinnisvara_vaartus() - BalanceAka42 - BalanceAka38
MorrKinnisvaraPort = 67700 - BalanceSõle # Sõle korteri hind - balance

print("\nHetkel korterite puhas väärtus kokku:", KinnisVaraPort, "€.")
KoikKokku = Valme.FysIsik + Valme.JurIsik + KinnisVaraPort

'#Ehk 1 000 000 Eesti krooni'
Eesmark = round(1000000/15.6466)
Eesmark2 = 500000
print("Vilde peale makse Isale:", colored(Valme.Uus_vilde_summa, 'red'), "€.")

print("Juriidilise isiku väärtus:", Valme.JurIsik, "€.")
print("Füüsilise isiku aktsia portfell:", Valme.FysIsik, "€.")
print("Aktsiad/Raha Jur ja Füs isikud kokku:", Valme.FysIsik + Valme.JurIsik, "€.")
print("Vaba raha Jur/Füs Kokku:", colored(Valme.RahaKokku, 'red'), "€.")
print("Funderbeam Kokku:", colored(Valme.JurFunderBeam, 'red'), "€.")
print("Terve portfell kokku:", colored(KoikKokku, 'red'), "€.")
print("Eesmärk krooni miljonär", Eesmark, "€.")
print("Krooni miljonär veel minna:", colored(Eesmark - KoikKokku, 'red'), "€.")

print("Eesmärk 35 aastaselt portfelli väärtus", Eesmark2, "€.")
print("Veel minna:", colored(Eesmark2 - KoikKokku, 'red'), "€.")

Morr_kokku = Morr.kokku + MorrKinnisvaraPort
print("Mörr-i aktsiad:",  Morr.kokku, "€.")
print("Mörr-i kinnisvara:", MorrKinnisvaraPort, "€.")
print("Mörr-i portfell:", colored(Morr_kokku, 'red'), "€.")
Pere = KoikKokku + Morr_kokku
print("Pere portfell kokku:", colored(Pere, 'red'), "€.")

Aktsiad_kokku = Valme.FysIsik+Valme.JurIsik
need_new_excel_file("Portfell", "Porfelli Info")

'#exceli_nimi, kinnisvara_puhas, füs_aktsiad, jur_aktsiad, aktsiad_kokku, kokku_portfell, pere portfell, Vilde, Vaba raha '
update_excel(path + 'Portfolio_calculator/', "Portfell",
             KinnisVaraPort, Valme.FysIsik, Valme.JurIsik, Aktsiad_kokku,
             KoikKokku, Morr_kokku, Pere, Valme.Uus_vilde_summa, Valme.RahaKokku)

'# for combining results to send in e-mail'
Tulemus = "\nTerve portfell kokku: " + str(KoikKokku) + " €." + \
          "\nEesmärk krooni miljonär " + str(Eesmark) + " €." + \
          "\nKrooni miljonär veel minna: " + str(Eesmark - KoikKokku) + " €." + \
          "\nEesmärk 35 aastaselt portfelli väärtus " + str(Eesmark2) + " €." + \
          "\nVeel minna: " + str(Eesmark2 - KoikKokku) + " €." + \
          "\nMörr-i aktsiad:" + str(Morr.kokku) + " €." + \
          "\nMörr-i kinnisvara:" + str(MorrKinnisvaraPort) + " €." + \
          "\nMörr-i portfell: " + str(Morr_kokku) + " €. " + \
          "\nPere portfell kokku: " + str(Pere) + " €." + "\n\n" +\
          "\nLaenu Akadeemia 42-63 makstud: " + str(dateAka42.years) + " Years, " + str(dateAka42.months) + " Months" +\
          "\nLaenu Akadeemia 38-20 makstud: " + str(dateAka38.years) + " Years, " + str(dateAka38.months) + " Months" +\
          "\nLaenu Vilde 90-193 makstud: " + str(dateVilde90.years) + " Years, " + str(dateVilde90.months) + " Months" +\
          "\nLaenu Sõle 25B/3-21 makstud: " + str(dateSõle.years) + " Years, " + str(dateSõle.months) + " Months"

'#if it is friday and password file is in directory, then send e-mail'
if os.path.isfile(what_path_for_file() + r'Send_Email\synology_pass'):

    no_file = 'E-maili saatmine: Parooli faili ei ole kataloogis: ' + what_path_for_file()
    no_file = colored(no_file, 'red')

elif date.today().weekday() == 4:

    '# Variables are: STMP, username, password file, send from, send to, email title and email body'
    Send.send_email('192.168.1.161', #'valme.noip.me',
                    'email',
                    what_path_for_file() + r'Send_Email\synology_pass',
                    'email@valme.noip.me',
                    'margit1986@gmail.com',
                    'Portfelli seis: ' + time.strftime('%d-%m-%Y'),
                    Tulemus)
else:
    print(colored('E-maili saatmine: Pole reede', 'green'))
