from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 4.721,
                   "EXSA": 26.917,
                   "EXXT": 11.46,
                   "SPYD": 	21.405,
                   "SPYW": 74.074
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 9000

m_aktsiad = round(Aktsiad.stocks_value_combined(morr_eur_stocks, True))

m_raha = 51660

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad)
