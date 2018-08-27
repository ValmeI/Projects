from lxml import html
import requests


def replace_with_zero(stat):
    '# to replace unknown stat (-) with zero.'
    if stat == "-":
        stat = 0
    return stat


def replace_comma(stat):
    '# removes comma in numbers. Is needed to convert to float. Numbers like 1,0000 and so on.'
    stat = str(stat)
    if "," in stat:
        stat = stat.replace(",", "")
        return stat
    else:
        return stat


def get_baltic_list_of_stocks():
    page = requests.get('https://fp.lhv.ee/market/baltic?region=BALTIC&currency=EUR')
    tree = html.fromstring(page.content)
    symbols = tree.xpath('//a[@class="stock-symbol"]/text()')  # pars symbol

    '# get last price. OR is for positive and negative tags '
    prices = tree.xpath('//td[@class="right no-wrap" '
                        'or @class="right no-wrap negative" '
                        'or @class="right no-wrap positive"]/text()')

    '# loop in to list and filter the right prices'
    prices_list = []

    for x in range(len(prices)):
        if x == 0 or (x % 5) == 0:
            prices_list.append(prices[x])

    '# zip together and convert to dictionary'
    zip_baltic_stocks_list = zip(symbols, prices_list)
    dic_baltic_stocks_list = dict(zip_baltic_stocks_list)

    return dic_baltic_stocks_list


def get_stock_fundamentals(sym):

    site = "https://www.lhv.ee/search/redirect.cfm?symbol=" + sym + "&mode=info"
    page = requests.get(site)
    tree = html.fromstring(page.content)

    report_url = tree.xpath('//a[contains(@href,"tab=reports")]/@href')
    '# return zeros if there is no nasdaq page'
    if not report_url:
        return 0, 0, 0, 0, 0, 0
    else:
        '#takes first element of the list'
        new_url = "http://www.nasdaqbaltic.com" + report_url[0]

        nasdaq_page = requests.get(new_url)

        nasdaq_tree = html.fromstring(nasdaq_page.content)
        morning_overview_url = nasdaq_tree.xpath('//a[contains(@href,"morningstar")]/@href')

        '# If stock do not have morning star page or morning star page is in source but does not exist.'
        '# return list on zeros'
        if not morning_overview_url or str(requests.get(morning_overview_url[0])) != "<Response [200]>":
            return 0, 0, 0, 0, 0, 0
        else:

            '''takes first element of the list'''
            morning_page = requests.get(morning_overview_url[0])
            morning_tree = html.fromstring(morning_page.content)
            price_earnings = morning_tree.xpath('//*[@id="KeyStatsPriceEarningRatio12M"]/td/text()')
            price_book = morning_tree.xpath('//*[@id="KeyStatsPriceBookRatio"]/td/text()')
            debt_equity = morning_tree.xpath('//*[@id="KeyStatsDebtEquity"]/td/text()')
            price_sales = morning_tree.xpath('//*[@id="KeyStatsPriceSalesRatio12M"]/td/text()')
            roe = morning_tree.xpath('//*[@id="KeyStatsReturnOnEquity12M"]/td/text()')

            '# to replace - with zero, so you can convert later stats to float'
            price_earnings[0] = replace_with_zero(price_earnings[0])
            price_book[0] = replace_with_zero(price_book[0])
            debt_equity[0] = replace_with_zero(debt_equity[0])
            price_sales[0] = replace_with_zero(price_sales[0])
            roe[0] = replace_with_zero(roe[0])

            '# replaces comma'
            price_earnings[0] = replace_comma(price_earnings[0])
            price_book[0] = replace_comma(price_book[0])
            debt_equity[0] = replace_comma(debt_equity[0])
            price_sales[0] = replace_comma(price_sales[0])
            roe[0] = replace_comma(roe[0])

            ''' [0] is to return element, without it it returns ['x'] and so on, it easier than to subtring '''
            return morning_overview_url[0], price_earnings[0], price_book[0], debt_equity[0], price_sales[0], roe[0]


def print_stats(stock):

    result = get_stock_fundamentals(stock)
    print("URL:", result[0])
    print("P/E:", result[1])
    print("P/B:", result[2])
    print("Debt/Equity:", result[3])
    print("Price/Sales:", result[4])
    print("ROE:", result[5])
    print("==================")


def get_market_capitalization():

    cap_dic = {}

    site = "http://www.nasdaqbaltic.com/market/?pg=capital&lang=en"
    page = requests.get(site)
    tree = html.fromstring(page.content)

    col_sym = str(2)
    col_cap = str(5)

    number_of_stocks = len(get_baltic_list_of_stocks().keys())

    '# starts from 1 and length of stock list'
    for cap in range(1, number_of_stocks):
        cap = str(cap)
        generated_path_cap = '//*[@id="marketBody"]/table[1]/tbody/tr[' + cap + ']/td[' + col_cap + ']/text()'
        generated_path_sym = '//*[@id="marketBody"]/table[1]/tbody/tr[' + cap + ']/td[' + col_sym + ']/text()'

        table_fields_caps = tree.xpath(generated_path_cap)
        table_fields_sym = tree.xpath(generated_path_sym)

        '# do not need nasdaq second list of stocks, so do not show empty results'
        if len(table_fields_sym) == 0 and len(table_fields_caps) == 0:
            continue

        '# to dictionary, 0 is needed to take 0 element form list'
        '# as tabel_fields_sym and tabel_fields_caps returns list '
        cap_dic[table_fields_sym[0]] = table_fields_caps[0]

    return cap_dic
