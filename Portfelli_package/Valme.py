from Portfelli_package import Aktsiad, Morr
from datetime import date


fys_eur_stocks = {"OLF1R": 67,
                  "SFG1T": 1668,
                  "TKM1T": 380,
                  "EFT1T": 66,
                  "TSM1T": 1000
                  }

jur_usa_stocks = {"AAPL": 15,
                  "TSLA": 6,
                  "AMD": 48,
                  "MSFT": 8,
                  "FB": 7
                  }

jur_eur_stocks = {"EFT1T": 51
                  }

'#Akadeemia laenu kuupäevad yyyy.mm.dd'
Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

FüsIsikRaha = 0
FysIsikAktsaid = Aktsiad.stocks_value_combined(fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)

JurAktsiad = Aktsiad.stocks_value_combined(jur_usa_stocks, False) + \
             Aktsiad.stocks_value_combined(jur_eur_stocks, True)

'#jur isiku raha LHV + LYNX RAHA'
JurRaha = 327.85
JurLynxRaha = 22.51
JurIsik = round(JurRaha + JurLynxRaha + JurAktsiad + Morr.ValCapitalRaha/2)

