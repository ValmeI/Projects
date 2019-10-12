from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 46,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.783,
                   "EXSA": 4.290,
                   "EXXT": 2.488,
                   "SPYD": 3.303,
                   "eudv?countrycode=fr": 10.553 #SPYW
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 4895

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 114.87

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)


