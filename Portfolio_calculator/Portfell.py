from Portfolio_calculator import Kinnisvara, Morr, Valme, txt_write_move, Kelly
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
'# Akadeemia 38-20 Müüdud 28.10.2021 Laenujääk 18 800 EUR'
PerMonthVilde90 = Kinnisvara.apr_month(Kinnisvara.Korter3_Laen, 2.39, 11)

print('\n' + Kinnisvara.Korter1_Nimi, "laenumakse:", PerMonthAka42, "€ + kindlustus.")
print(Kinnisvara.Korter3_Nimi, "laenumakse:", PerMonthVilde90, "€ + kindlustus.\n")

'# how many years and months each loan is paid already'
dateAka42 = relativedelta(Täna, Valme.Vana_Aka42_63_Laen_Kuupäev)
dateVilde90 = relativedelta(Täna, Valme.Vilde90_193_Laen_Kuupäev)

print("Laenu Akadeemia 42-63 makstud:", dateAka42.years, "Years,", dateAka42.months, "Months")
print("Laenu Vilde 90-193 makstud:", dateVilde90.years, "Years,", dateVilde90.months, "Months\n")

'#makstud kuude vahe arvutus'
KuudMakstudAka42 = diff_months(Täna, Valme.Aka42_63_Laen_Kuupäev)
KuudMakstudVilde90 = diff_months(Täna, Valme.Vilde90_193_Laen_Kuupäev)

'#diffMonths annab natuke erineva tulemuse, kui aastad vs kuud'
BalanceAka42 = Kinnisvara.apr_balance(Kinnisvara.Korter1_Laen, 3, 15, KuudMakstudAka42)
BalanceVilde90 = Kinnisvara.apr_balance(Kinnisvara.Korter3_Laen, 2.39, 11, KuudMakstudVilde90)

print(Kinnisvara.Korter1_Nimi, "laenu jääk", BalanceAka42, "€.", 'Laenu summa', Kinnisvara.Korter1_Laen)
print(Kinnisvara.Korter3_Nimi, "laenu jääk", BalanceVilde90, "€.", 'Laenu summa', Kinnisvara.Korter3_Laen)

print("\nLaenu kohutus kokku(ainult Akadeemia):", BalanceAka42)
print("Laenu kohutus kokku(Kõik):", BalanceAka42 + BalanceVilde90)

'#Kinnisvara kokku. Liidetakse kõik Dics korterite ostu hinnad - balancid ehk palju laenu veel maksta'
KinnisVaraPort = Kinnisvara.kinnisvara_vaartus() - BalanceAka42
#MorrKinnisvaraPort = 67700 - BalanceSõle

print("\nHetkel korterite puhas väärtus kokku:", KinnisVaraPort, "€.")

'# Portfell kokku'
Ignar_Kokku = Valme.FysIsik + Valme.JurIsik + KinnisVaraPort

'#Ehk 1 000 000 Eesti krooni'
Eesmark = round(1000000/15.6466)
Eesmark2 = 500000
print("Vilde peale makse Isale:", colored(Valme.Uus_vilde_summa, 'red'), "€.")
print("\n")
print("Juriidilise isiku väärtus:", Valme.JurIsik, "€.")
print("Krüpto:", colored(Valme.Jur_Krypto, 'red'), "€.")
print("Juriidilise isiku aktsiad:", Valme.JurAktsiad, "€.")
print("Funderbeam Kokku:", colored(Valme.JurFunderBeam, 'red'), "€.")
print("\n")
print("Füüsilise isiku aktsia portfell:", Valme.FysIsik, "€.")
print("Aktsiad/Raha Jur ja Füs isikud kokku:", Valme.FysIsik + Valme.JurIsik, "€.")
print("Vaba raha Jur/Füs Kokku:", colored(Valme.RahaKokku, 'red'), "€.")
print("\n")
print("Terve portfell kokku:", colored(Ignar_Kokku, 'red'), "€.")
print("Eesmärk krooni miljonär", Eesmark, "€.")
print("Krooni miljonär veel minna:", colored(Eesmark - Ignar_Kokku, 'red'), "€.")

print("Eesmärk 35 aastaselt portfelli väärtus", Eesmark2, "€.")
print("Veel minna:", colored(Eesmark2 - Ignar_Kokku, 'red'), "€.")

Morr_kokku = Morr.kokku #+ MorrKinnisvaraPort
print("Mörr-i aktsiad:",  Morr.m_aktsiad, "€.")
print("Mörr-i vaba raha:",  Morr.m_raha, "€.")
#print("Mörr-i kinnisvara:", MorrKinnisvaraPort, "€.")
print("Mörr-i portfell kokku:", colored(Morr_kokku, 'red'), "€.")

'# Kelly Portfell'
Kelly_kokku = Kelly.Kelly_Portfell_Kokku
print("Kelly portfell:", colored(Kelly_kokku, 'red'), "€.")

'# Pere kõik kokku'
Pere = Ignar_Kokku + Morr_kokku + Kelly_kokku
print("Pere portfell kokku:", colored(Pere, 'red'), "€.")

Aktsiad_kokku = Valme.FysIsik+Valme.JurIsik
need_new_excel_file("Portfell", "Porfelli Info")

'#exceli_nimi, kinnisvara_puhas, füs_aktsiad, jur_aktsiad, aktsiad_kokku, kokku_portfell, pere portfell, Vilde, Vaba raha, Funderbeam, Kelly '
update_excel(path + 'Portfolio_calculator/', "Portfell",
             KinnisVaraPort, Valme.FysIsik, Valme.JurIsik, Aktsiad_kokku,
             Ignar_Kokku, Morr_kokku, Pere, Valme.Uus_vilde_summa, Valme.RahaKokku, Valme.JurFunderBeam, Kelly_kokku)

'# for combining results to send in e-mail'
Tulemus = "\nTerve portfell kokku: " + str(Ignar_Kokku) + " €." + \
          "\nEesmärk krooni miljonär: " + str(Eesmark) + " €." + \
          "\nKrooni miljonär veel minna: " + str(Eesmark - Ignar_Kokku) + " €." + \
          "\nEesmärk 35 aastaselt portfelli väärtus: " + str(Eesmark2) + " €." + \
          "\nVeel minna: " + str(Eesmark2 - Ignar_Kokku) + " €." + \
          "\nMörr-i aktsiad: " + str(Morr.m_aktsiad) + " €." + \
          "\nMörr-i vaba raha: " + str(Morr.m_raha) + " €." + \
          "\nMörr-i portfell kokku: " + str(Morr_kokku) + " €. " \
          "\nKelly portfell: " + str(Kelly_kokku) + " €. " + \
          "\nPere portfell kokku: " + str(Pere) + " €." + "\n\n" +\
          "\nLaenu Akadeemia 42-63 makstud: " + str(dateAka42.years) + " Years, " + str(dateAka42.months) + " Months" +\
          "\nLaenu Vilde 90-193 makstud: " + str(dateVilde90.years) + " Years, " + str(dateVilde90.months) + " Months" +\
          "\n\n" + str(Kinnisvara.Korter1_Nimi) + " laenu jääk " + str(BalanceAka42) + " €." + ' Laenu summa ' + str(Kinnisvara.Korter1_Laen) +\
          "\n" + str(Kinnisvara.Korter3_Nimi) + " laenu jääk " + str(BalanceVilde90) + " €." + ' Laenu summa ' + str(Kinnisvara.Korter3_Laen)

'#if it is friday and password file is in directory, then send e-mail'
if os.path.isfile(what_path_for_file() + r'Send_Email\synology_pass'):

    no_file = 'E-maili saatmine: Parooli faili ei ole kataloogis: ' + what_path_for_file()
    no_file = colored(no_file, 'red')

elif date.today().weekday() == 4:

    '# Variables are: STMP, username, password file, send from, send to, email title and email body'
    Send.send_email('192.168.1.172', #'valme.noip.me',
                    'email',
                    what_path_for_file() + r'Send_Email\synology_pass',
                    'email@valme.noip.me',
                    'val-capital@googlegroups.com',
                    'Portfelli seis: ' + time.strftime('%d-%m-%Y'),
                    Tulemus)
else:
    print(colored('E-maili saatmine: Pole reede', 'green'))
