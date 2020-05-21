from Portfolio_calculator import Aktsiad
from datetime import date


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 1.454,
                   "EXSA": 8.009,
                   "EXXT": 4.403,
                   "SPYD": 	6.140,
                   "SPYW": 19.979
                   }

'''morr_usa_stocks = {}'''

Sõle_Laen_Kuupäev = date(2011, 8, 25)

ValCapitalRaha = 5100

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 143.77

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


