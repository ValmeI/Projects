from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 35,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.278,
                   "EXSA": 1.510,
                   "EXXT": 0.893,
                   "SPYD": 1.163,
                   "SPYW": 3.730
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 3670

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 94.71

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


