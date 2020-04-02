from Portfolio_calculator import Aktsiad
from datetime import date


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 1.243,
                   "EXSA": 6.855,
                   "EXXT": 3.865,
                   "SPYD": 	5.249,
                   "SPYW": 16.948
                   }

'''morr_usa_stocks = {}'''

Sõle_Laen_Kuupäev = date(2011, 8, 25)

ValCapitalRaha = 6100

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 106.98

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


