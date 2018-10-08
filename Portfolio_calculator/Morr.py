from Portfolio_calculator import Aktsiad

morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 35,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 0.395,
                   "EXSA": 19.482,
                   "EXXT": 0.920,
                   "SPYW": 5.629
                   }

morr_usa_stocks = {"SPYD": 1.214,
                   "IVV": 7.076
                   }

ValCapitalRaha = 2260

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True) + \
            Aktsiad.stocks_value_combined(morr_usa_stocks, False)

m_raha = 96.37

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)

