from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.496,
                   "EXSA": 2.714,
                   "EXXT": 1.595,
                   "SPYD": 2.094,
                   "SPYW": 6.701
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 4095

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 115.66

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


