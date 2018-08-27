from Baltic_Stock_Screener import Baltic_List, Funcions

'# filter parameters'

'# lower than'
PE = 200
'# lower than'
PB = 1.5
'# bigger than'
ROE = 9
write_file = True
file_name = "Results"


print("\n-------------START-------------")

'# Empty a file'
if write_file:
    Funcions.empty_file(file_name)

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

        #if key == k:
        #print("Stock Symbol:", key, "= P/B:", price_book, "= P/E:", price_earnings, "= ROE:", roe, "= Market Cap:", v)

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
            if write_file:
                Funcions.write_to_file(file_name,
                                       "Stock Symbol: " + str(key),
                                       "\n= P/B: " + str(price_book),
                                       "\n= P/E: " + str(price_earnings),
                                       "\n= ROE: " + str(roe),
                                       "\n= Market Cap: " + str(v) + "\n")

print("-------------END-------------")












