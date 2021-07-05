from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 2.713,
                   "EXSA": 15.440,
                   "EXXT": 7.301,
                   "SPYD": 	12.070,
                   "SPYW": 40.606
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 8200

m_aktsiad = Aktsiad.stocks_value_combined(morr_eur_stocks, True)

m_raha = 56500

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
