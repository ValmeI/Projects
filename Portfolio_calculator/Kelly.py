from Portfolio_calculator import Aktsiad


ETH_amount = 0.10581

ETH_USD = Aktsiad.crypto_price_from_coingecko('ethereum') * ETH_amount
ETH_EUR = Aktsiad.usd_to_eur_convert(ETH_USD)

Kelly_raha = 43.87

Kelly_Portfell_Kokku = Kelly_raha + ETH_EUR