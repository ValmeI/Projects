from Project_Baltic_Stocks import Baltic_List, Funcions

'Porgrammi kasutamiseks pane Main.py tööle'


print("\nBalti aktsiate filtreeria (hinna/kasumi suhe, "
      "raamatupidamise väärtus ja omakapitali tootlus) \n")

PE = int(input("Palun sisestage balti aktsia hinna ja kasumi (PE) filtreerimise parameeter (näiteks 50): "))
PB = int(input("Palun sisestage balti aktsia raamatupidamis väärtuse (PB) filtreerimise parameeter (näiteks 10): "))
ROE = int(input("Palun sisestage balti aktsia omakapitali tootluse (ROE) filtreerimise parameeter (näiteks 1): "))
kas_faili = (input("Kas soovite tulemused kirjutada faili? (JAH/EI): "))

print("\n-------------START-------------")

'# take Baltic stock list and get fundamentals'
for key in Baltic_List.get_baltic_list_of_stocks().keys():
    price_earnings = Baltic_List.get_stock_fundamentals(key)[1]
    price_earnings = float(price_earnings)

    price_book = Baltic_List.get_stock_fundamentals(key)[2]
    price_book = float(price_book)

    roe = Baltic_List.get_stock_fundamentals(key)[5]
    roe = float(roe)

    '# get market cap dictionary and match with stock list'
    for k, v in Baltic_List.get_market_capitalization().items():

        '# filter what to print and so on'
        if key == k \
                and price_book < PB \
                and price_book != 0.0 \
                and price_earnings < PE \
                and roe > ROE:

            print("Stock Symbol:", key,
                  "\n= P/B:", price_book,
                  "\n= P/E:", price_earnings,
                  "\n= ROE:", roe,
                  "\n= Market Cap:", v, "\n")

            '# check if user wants to write data to file'
            if kas_faili.upper() == "JAH":

                Funcions.write_to_fail("file",
                                       "Stock Symbol: " + str(key),
                                       "\n= P/B: " + str(price_book),
                                       "\n= P/E: " + str(price_earnings),
                                       "\n= ROE: " + str(roe),
                                       "\n= Market Cap: " + str(v) + "\n")


print("-------------END-------------")












