from Portfolio_calculator import Aktsiad, Morr
from datetime import date


fys_eur_stocks = {"OLF1R": 67,
                  "SFG1T": 1668,
                  "TKM1T": 316,
                  "EFT1T": 66,
                  "TSM1T": 1000
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

# TODO how to calculate dividens, add needed funcions
'#Vanad ja refinants Akadeemia laenu kuupäevad yyyy.mm.dd'
Vana_Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Vana_Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

Aka42_63_Laen_Kuupäev = date(2018, 12, 5)
Aka38_20_Laen_Kuupäev = date(2018, 12, 5)

FüsIsikRaha = 48.75
FysIsikAktsaid = Aktsiad.stocks_value_combined(fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)

JurAktsiad = Aktsiad.stocks_value_combined(jur_usa_stocks, False) + Aktsiad.stocks_value_combined(jur_eur_stocks, True)

'#jur isiku raha LHV + LYNX RAHA'
JurRaha = 314.89
JurLynxRaha = 16
JurIsik = round(JurRaha + JurLynxRaha + JurAktsiad + Morr.ValCapitalRaha/2)
#Mörr on väike karu

