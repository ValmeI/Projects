from Portfolio_calculator import Aktsiad


ETH_amount = 0.10581

ETH_USD = Aktsiad.crypto_price_from_coinmarketcap('ethereum') * ETH_amount
ETH_EUR = Aktsiad.usd_to_eur_convert(ETH_USD)

Kelly_raha = 0
Kelly_Invest_raha = 200

Kelly_Portfell_Kokku = round(Kelly_raha + Kelly_Invest_raha + ETH_EUR)
