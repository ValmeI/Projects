def write_to_file(file_name, key, price_book, price_earnings, roe, market_cap):
    '# write every row to new line (a)'
    with open(file_name + ".txt", 'a') as f:
        f.write(key)
        f.write(price_book)
        f.write(price_earnings)
        f.write(roe)
        f.write(market_cap + "\n")


def empty_file(file_name):
    '# emptyh a file. Open and close'
    with open(file_name + ".txt", 'w') as f:
        f.close()


