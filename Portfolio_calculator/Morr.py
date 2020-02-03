from Portfolio_calculator import Aktsiad
from datetime import date


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 1.070,
                   "EXSA": 5.891,
                   "EXXT": 3.364,
                   "SPYD": 	4.503,
                   "SPYW": 14.516
                   }

'''morr_usa_stocks = {}'''

Sõle_Laen_Kuupäev = date(2011, 8, 25)

ValCapitalRaha = 5695

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 108.37

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


