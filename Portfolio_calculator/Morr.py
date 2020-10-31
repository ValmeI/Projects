from Portfolio_calculator import Aktsiad
from datetime import date


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 2.039,
                   "EXSA": 11.460,
                   "EXXT": 5.768,
                   "SPYD": 	8.902,
                   "SPYW": 29.227
                   }

'''morr_usa_stocks = {}'''

Sõle_Laen_Kuupäev = date(2011, 8, 25)

ValCapitalRaha = 7100

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 228.11

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
