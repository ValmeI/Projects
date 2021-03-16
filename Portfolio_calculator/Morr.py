from Portfolio_calculator import Aktsiad
from datetime import date


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 2.133,
                   "EXSA": 12.012,
                   "EXXT": 5.969,
                   "SPYD": 	9.337,
                   "SPYW": 30.792
                   }

'''morr_usa_stocks = {}'''

Sõle_Laen_Kuupäev = date(2011, 8, 25)

ValCapitalRaha = 7000

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 227

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
