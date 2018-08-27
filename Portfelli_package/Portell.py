from Portfelli_package import Kinnisvara, Funcions, Aktsiad
from datetime import date
from dateutil.relativedelta import relativedelta


'# tänane kuupäev arvutamaks, et mitu makset on tehtud juba'
Täna = date.today()

'#Akadeemia laenu kuupäevad yyyy.mm.dd'
Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

'#Kinnisvara objetktide print'
Kinnisvara.korterid()
PerMonthAka42 = Kinnisvara.apr_month(Kinnisvara.Korter1_Laen, 2.75, 15)
PerMonthAka38 = Kinnisvara.apr_month(Kinnisvara.Korter2_Laen, 3.7, 15)

print(Kinnisvara.Korter1_Nimi, "laenumakse:", PerMonthAka42, "€.")
print(Kinnisvara.Korter2_Nimi, "laenumakse:", PerMonthAka38, "€.")

'#makstud kuude vahe arvutus'
KuudMakstudAka42 = Funcions.diff_months(Täna, Aka42_63_Laen_Kuupäev)
KuudMakstudAka38 = Funcions.diff_months(Täna, Aka38_20_Laen_Kuupäev)

'# how many years and months each loan is paid already'
dateAka42 = relativedelta(Täna, Aka42_63_Laen_Kuupäev)
dateAka38 = relativedelta(Täna, Aka38_20_Laen_Kuupäev)
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


FüsIsikRaha = 0
FysIsikAktsaid = Aktsiad.stocks_value_combined(Aktsiad.fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)


JurAktsiad = Aktsiad.stocks_value_combined(Aktsiad.jur_usa_stocks, False) + \
             Aktsiad.stocks_value_combined(Aktsiad.jur_eur_stocks, True)

'#jur isiku raha LHV + LYNX RAHA'
JurRaha = 1340.94
JurLynxRaha = 197.07
JurIsik = round(JurRaha + JurLynxRaha + JurAktsiad)

KoikKokku = FysIsik + JurIsik + KinnisVaraPort
'#Ehk 1 000 000 Eesti krooni'
Eesmark = round(1000000/15.6466)

print("Juriidilise isiku väärtus:", JurIsik, "€.")
print("Füüsilise isiku aktsia portfell:", FysIsik, "€.")
print("Aktsiad/Raha Jur ja Füs isikud kokku:", FysIsik + JurIsik, "€.")

print("Terve portfell kokku:", KoikKokku, "€.")
print("Eesmärk krooni miljonär", Eesmark, "€.")
print("Veel minna", Eesmark - KoikKokku, "€.")

Funcions.need_new_excel_file("Portfell")

'#exceli_nimi, kinnisvara_puhas, füs_aktsiad, jur_aktsiad, aktsiad_kokku, kokku_portfell'
Funcions.update_excel("Portfell", KinnisVaraPort, FysIsik, JurIsik, FysIsik+JurIsik, KoikKokku)

'#TODO - pere sektor koos väärtuse jälgimisega'
