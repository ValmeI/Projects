from Portfolio_calculator import Aktsiad

jur_eur_stocks = {
                  "EGR1T": 172,
                  "HPR1T": 23
                 }

ETH_amount = 0.10581

ETH_USD = Aktsiad.crypto_to_eur('Ethereum') * ETH_amount
ETH_EUR = Aktsiad.usd_to_eur_convert(ETH_USD)

Kelly_raha = 0
Kelly_Invest_raha = 50.97 + 330.75 #textmagic
Kelly_Invest_aktsiad = Aktsiad.stocks_value_combined(jur_eur_stocks, True)

Kelly_Portfell_Kokku = round(Kelly_raha + Kelly_Invest_raha + ETH_EUR + Kelly_Invest_aktsiad)

