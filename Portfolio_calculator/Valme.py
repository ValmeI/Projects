from Portfolio_calculator import Aktsiad, Morr, Funcions as f
from datetime import date


fys_eur_stocks = {"OLF1R": 67,
                  "SFG1T": 1668,
                  "TKM1T": 316,
                  "EFT1T": 66,
                  "TSM1T": 1000,
                  "BLT1T": 333
                  }

jur_usa_stocks = {"AAPL": 15,
                  "TSLA": 6,
                  "AMD": 48,
                  "MSFT": 8,
                  "FB": 7,
                  "AMZN": 1,
                  "XIACY": 5
                  }

jur_eur_stocks = {"SXR8": 2}

'#Vanad ja refinants Akadeemia laenu kuupäevad yyyy.mm.dd'
Vana_Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Vana_Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

Aka42_63_Laen_Kuupäev = date(2018, 12, 5)
Aka38_20_Laen_Kuupäev = date(2018, 12, 5)
Vilde90_193_Laen_Kuupäev = date(2019, 4, 9)

FüsIsikRaha = 223.39
FysIsikAktsaid = Aktsiad.stocks_value_combined(fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)

JurAktsiad = Aktsiad.stocks_value_combined(jur_usa_stocks, False) + Aktsiad.stocks_value_combined(jur_eur_stocks, True)

'#jur isiku raha LHV + LYNX RAHA'
JurRaha = 1227.08
JurLynxRaha = 19
JurIsik = round(JurRaha + JurLynxRaha + JurAktsiad + Morr.ValCapitalRaha/2)
#Mörr on väike karu

vilde_isa = 230 # üür
vilde_laen = 154.88
vilde_kindlustus = 6.91
arvutamise_kp = 1 # ehk kuu päev millal

Uus_vilde_summa = f.vilde_calculation(arvutamise_kp,
                                      f.get_last_row("Portfell", 9),
                                      round(f.dividend_with_certain_date(vilde_isa) - vilde_laen - vilde_kindlustus, 2),
                                      f.get_last_row("Portfell", 1)
                                      )
