from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EGR1T": 1000,
                   "EXS1": 13.963,
                   "EXSA": 79.215,
                   "EXXT": 29.857,
                   "SPYD": 62.090,
                   "SPYW": 235.066
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 10300

Lähtse_Raha = 20000

m_aktsiad = round(Aktsiad.stocks_value_combined(morr_eur_stocks, True))

m_raha = 28343.33

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad + Lähtse_Raha/2)
