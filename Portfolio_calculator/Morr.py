from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 35,
                   "TKM1T": 53,
                   "TSM1T": 560
                   }

'''morr_usa_stocks = {}'''

ValCapitalRaha = 2860

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 158.82

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)

