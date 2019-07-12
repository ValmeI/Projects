from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.589,
                   "EXSA": 3.232,
                   "EXXT": 1.893,
                   "SPYD": 2.497,
                   "SPYW": 7.983
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 4295

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 115.96

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


