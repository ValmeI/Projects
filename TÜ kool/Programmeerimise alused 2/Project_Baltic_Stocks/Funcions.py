def write_to_fail(faili_nimi, key, price_book, price_earnings, roe, v):

    '# write every row to new line'

    with open(faili_nimi + ".txt", 'a') as f:
        f.write(key)
        f.write(price_book)
        f.write(price_earnings)
        f.write(roe)
        f.write(v + "\n")
