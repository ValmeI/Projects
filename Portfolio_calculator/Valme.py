from Portfolio_calculator import Aktsiad, Morr, Funcions as f
from datetime import date
from Portfolio_calculator.Funcions import what_path_for_file

path = what_path_for_file()

fys_eur_stocks = {"SFG1T": 1668,
                  "TKM1T": 355,
                  "EFT1T": 94,
                  "TSM1T": 1286
                  }

jur_usa_stocks = {"AAPL": 15,
                  "TSLA": 6,
                  "AMD": 88,
                  "MSFT": 12,
                  "FB": 7,
                  "AMZN": 1,
                  "XIACY": 23
                  }

jur_eur_stocks = {"SXR8": 5}

'#Vanad ja refinants Akadeemia laenu kuupäevad yyyy.mm.dd'
Vana_Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Vana_Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

Aka42_63_Laen_Kuupäev = date(2018, 12, 5)
Aka38_20_Laen_Kuupäev = date(2018, 12, 5)
Vilde90_193_Laen_Kuupäev = date(2019, 4, 9)

FüsIsikRaha = 9.72
FysIsikAktsaid = Aktsiad.stocks_value_combined(fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)

JurAktsiad = Aktsiad.stocks_value_combined(jur_usa_stocks, False) + Aktsiad.stocks_value_combined(jur_eur_stocks, True)

'#jur isiku raha LHV + LYNX RAHA'
JurRaha = 48.79
JurFunderBeam = 3513.88
JurLynxRaha = 22
JurIsik = round(JurRaha + JurFunderBeam + JurLynxRaha + JurAktsiad + Morr.ValCapitalRaha/2)
'# Mörr on väike karu'

'# üür'
vilde_isa = 250
vilde_laen = 154.88
vilde_kindlustus = 6.91
'# ehk kuupäev millal arvutust tehakse'
arvutamise_kp = 1

Uus_vilde_summa = f.vilde_calculation(arvutamise_kp,
                                      f.get_last_row(path + 'Portfolio_calculator/', "Portfell", 9),
                                      round(f.dividend_with_certain_date(vilde_isa) - vilde_laen - vilde_kindlustus, 2),
                                      f.get_last_row(path + 'Portfolio_calculator/', "Portfell", 1)
                                      )

'# to avoid too many decimal places'
Uus_vilde_summa = round(Uus_vilde_summa, 2)
