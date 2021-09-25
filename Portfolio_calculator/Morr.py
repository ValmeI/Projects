from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 4.914,
                   "EXSA": 28.030,
                   "EXXT": 11.864,
                   "SPYD": 	22.314,
                   "SPYW": 77.320
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 8600

m_aktsiad = round(Aktsiad.stocks_value_combined(morr_eur_stocks, True))

m_raha = 51506.58

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
