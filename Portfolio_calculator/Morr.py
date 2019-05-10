from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 35,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.400,
                   "EXSA": 2.186,
                   "EXXT": 1.279,
                   "SPYD": 1.684,
                   "SPYW": 5.417
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 3895

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 164.25

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


