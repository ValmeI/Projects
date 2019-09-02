from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.687,
                   "EXSA": 3.772,
                   "EXXT": 2.197,
                   "SPYD": 2.907,
                   "SPYW": 9.270
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 4695

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 114.87

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


