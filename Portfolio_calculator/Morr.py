from Portfolio_calculator import Aktsiad


morr_eur_stocks = {"APG1L": 196,
                   "EFT1T": 55,
                   "TKM1T": 53,
                   "TSM1T": 560,
                   "EXS1": 11.794,
                   "EXSA": 66.941,
                   "EXXT": 25.537,
                   "SPYD": 52.821,
                   "SPYW": 196.987,
                   "EGR1T": 1000,
                   "HPR1T": 30
                   }

'''morr_usa_stocks = {}'''

'''Sõle_Laen_Kuupäev = date(2011, 8, 25) #Müüdud 22.06.2021'''

ValCapitalRaha = 10100

Lähtse_Raha = 20000

m_aktsiad = round(Aktsiad.stocks_value_combined(morr_eur_stocks, True))

m_raha = 30422.35

kokku = round(ValCapitalRaha/2 + m_raha + m_aktsiad + Lähtse_Raha/2)
