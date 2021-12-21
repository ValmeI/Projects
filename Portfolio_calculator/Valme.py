from Portfolio_calculator import Aktsiad, Morr, Funcions as f
from datetime import date
from Portfolio_calculator.Funcions import what_path_for_file

path = what_path_for_file()

fys_eur_stocks = {"TKM1T": 355,
                  "EFT1T": 113,
                  "EGR1T": 500,
                  "HPR1T": 89
                  }

jur_usa_stocks = {"AAPL": 93,
                  "TSLA": 8,
                  "AMD": 84,
                  "MSFT": 12,
                  "AMZN": 3,
                  "GOOGL": 2,
                  "NIO": 93,
                  "XPEV": 72,
                  "PLTR": 50,
                  "NKE": 11,
                  "NFLX": 1,
                  "NVDA": 1
                  }

jur_eur_stocks = {
                  "EGR1T": 1115, #LHV
                  "EGR1T": 400, #IB
                  "HPR1T": 61,
                  "LHV1T": 100
                  }

'# Crypto Amounts'
BTC_amount = 0.021538
Million_Coin_amount = 7.125
ETH_amount = 0.16298

'# All crypto and to EUR from USD'
Million_Coin_USD = Aktsiad.crypto_price_from_coinmarketcap('million') * Million_Coin_amount
Million_Coin_EUR = Aktsiad.usd_to_eur_convert(Million_Coin_USD)

ETH_USD = Aktsiad.crypto_price_from_coinmarketcap('ethereum') * ETH_amount
ETH_EUR = Aktsiad.usd_to_eur_convert(ETH_USD)

Bitcoin_USD = Aktsiad.crypto_price_from_coinmarketcap('bitcoin') * BTC_amount
Bitcoin_EUR = Aktsiad.usd_to_eur_convert(Bitcoin_USD)

'#Vanad ja refinants Akadeemia laenu kuupäevad yyyy.mm.dd'
Vana_Aka42_63_Laen_Kuupäev = date(2016, 2, 16)
Vana_Aka38_20_Laen_Kuupäev = date(2017, 5, 9)

Aka42_63_Laen_Kuupäev = date(2018, 12, 5)
#Aka38_20_Laen_Kuupäev = date(2018, 12, 5)
Vilde90_193_Laen_Kuupäev = date(2019, 4, 9)

FüsIsikRaha = 1972+343#textmagic
FysIsikAktsaid = Aktsiad.stocks_value_combined(fys_eur_stocks, True)

'# Vaba raha ja aktsiad kokku'
FysIsik = round(FüsIsikRaha + FysIsikAktsaid)

CleveronAktsia = 4 * 850
JurAktsiad = round(Aktsiad.stocks_value_combined(jur_usa_stocks, False) +
                   Aktsiad.stocks_value_combined(jur_eur_stocks, True) + CleveronAktsia)

Jur_Krypto = round(Bitcoin_EUR + Million_Coin_EUR + ETH_EUR)

'#jur isiku raha LHV + IB RAHA'
JurRaha = 14800
'# get Funderbeam total'
JurFunderBeam = f.get_funderbeam_marketvalue()
Jur_IB_Raha = -13000
JurIsik = round(JurRaha + JurFunderBeam + Jur_IB_Raha + JurAktsiad + Morr.ValCapitalRaha / 2 + Jur_Krypto)
'# Mörr on väike karu'


'# Raha ehk likviitsus,ka Krypto, jur ja fys kokku'
RahaKokku = round(FüsIsikRaha + JurRaha + Morr.ValCapitalRaha / 2 + Jur_IB_Raha + Jur_Krypto)

'# üür'
vilde_isa = 200
vilde_laen = 154.88
vilde_kindlustus = 6.91
'# ehk kuupäev millal arvutust tehakse'
arvutamise_kp = 1

Uus_vilde_summa = f.vilde_calculation(arvutamise_kp,
                                      f.get_last_row(path + 'Portfolio_calculator/', "Portfell", 9),
                                      round(f.dividend_with_certain_date(vilde_isa) - vilde_laen - vilde_kindlustus, 2),
                                      f.get_last_row(path + 'Portfolio_calculator/', "Portfell", 1)
                                      )

'# to avoid too many decimal places'
Uus_vilde_summa = round(Uus_vilde_summa, 2)
