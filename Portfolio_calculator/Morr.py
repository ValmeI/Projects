from Portfolio_calculator import Aktsiad
from datetime import date


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 1.843,
                   "EXSA": 10.260,
                   "EXXT": 5.323,
                   "SPYD": 	7.933,
                   "SPYW": 25.953
                   }

'''morr_usa_stocks = {}'''

Sõle_Laen_Kuupäev = date(2011, 8, 25)

ValCapitalRaha = 3400

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 230.67

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
