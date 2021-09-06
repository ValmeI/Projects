from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 2.864,
                   "EXSA": 16.318,
                   "EXXT": 7.627,
                   "SPYD": 	12.775,
                   "SPYW": 43.179
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 8900

m_aktsiad = round(Aktsiad.stocks_value_combined(morr_eur_stocks, True))

m_raha = 54160

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
