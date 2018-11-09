from Portfolio_calculator import Aktsiad, Morr
from datetime import date


fys_eur_stocks = {"OLF1R": 67,
                  "SFG1T": 1668,
                  "TKM1T": 150,
                  "EFT1T": 66,
                  "TSM1T": 1000
                  }

jur_usa_stocks = {"AAPL": 15,
                  "TSLA": 6,
                  "AMD": 48,
                  "MSFT": 8,
                  "FB": 7,
                  "AMZN": 1
                  }


'#Akadeemia laenu kuupäevad yyyy.mm.dd'
Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

FüsIsikRaha = 2015.14
FysIsikAktsaid = Aktsiad.stocks_value_combined(fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)

JurAktsiad = Aktsiad.stocks_value_combined(jur_usa_stocks, False)

'#jur isiku raha LHV + LYNX RAHA'
JurRaha = 211.28
JurLynxRaha = 80
JurIsik = round(JurRaha + JurLynxRaha + JurAktsiad + Morr.ValCapitalRaha/2)

