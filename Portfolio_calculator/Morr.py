from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 7.258,
                   "EXSA": 41.364,
                   "EXXT": 16.714,
                   "SPYD": 	32.773,
                   "SPYW": 117.500,
                   "EGR1T": 1000
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 9200

Lähtse_Raha = 20000

m_aktsiad = round(Aktsiad.stocks_value_combined(morr_eur_stocks, True)) + 400 #Hepsor

m_raha = 29138.72

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad + Lähtse_Raha/2)
