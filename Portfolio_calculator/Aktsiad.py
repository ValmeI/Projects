from lxml import html
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def replace_comma(stat):
    '# removes comma in numbers. Is needed to convert to float. Numbers like 1,0000 and so on.'
    stat = str(stat)
    if "," in stat:
        stat = stat.replace(",", "")
        return stat
    else:
        return stat


def stock_price_from_market_watch(stock, original_currency):

    url = "https://www.marketwatch.com/search?q=" + stock
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price_org_currency = tree.xpath('//p[@class="data bgLast"]/text()')

    '# UPDATE 6.08.2018 part of website updating most of it''s loading to JS, code was changed to use url of search '
    '# UPDATE 6.08.2018 and parse price from there and span part was not necessary anymore '

    '# convert so string and remove bracelets'
    str_price_org_currency = str(price_org_currency)[2:-2]

    if original_currency:
        '#Returns original currency'
        str_price_org_currency = replace_comma(str_price_org_currency)
        return float(str_price_org_currency)
    else:
        '#Converts and Returns currency in euros'

        '# UPDATE 25.08.2018 USD to EUR converting page started using JS and I needed to use Selenium and Soup but'
        '# UPDATE 25.08.2018 opening every page in Chrome and parsing made it much more slower'
        '# use page to convert USD to EUR'
        convert_url = "http://www.xe.com/currencyconverter/convert/?Amount=" + str_price_org_currency + "&From=USD&To=EUR"

        '# add options to chrome, to run it headless as not opening it'
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Chrome(r"D:\PycharmProjects\Projects\chromedriver.exe", options=options)
        driver.get(convert_url)

        convert_html = driver.page_source
        '# scrape with BeautifulSoup'
        soup = BeautifulSoup(convert_html, 'lxml')
        '# specify of what tag and what class, to get results in euros'
        to_eur_convert = soup.find('span', class_='converterresult-toAmount').text
        to_eur_convert = replace_comma(to_eur_convert)
        return float(to_eur_convert)


'#Stock list input and True/False as do you want it to bet original currency or in euros'


def stocks_value_combined(stock_dictionary, org_currency):
    total_value = 0
    for sym, amount in stock_dictionary.items():
        price = stock_price_from_market_watch(sym, org_currency)
        value = price * amount
        total_value += value
    return total_value


'#Single stock price, input symbol, org_currency = True/False and stock dictionary'


def stock_amount_value(stock_symbol, org_currency, stocks_dictionary):
        amount = stocks_dictionary[stock_symbol]
        price = stock_price_from_market_watch(stock_symbol, org_currency)
        value = price * amount
        return value


'#  Portfolio stocks %, input: Portfolio size, stock dictionary, org_currency = True/False'


def stocks_portfolio_percentages(portfolio_size, stocks_dictionary, org_currency):
    for sym, amount in stocks_dictionary.items():
        value = stock_amount_value(sym, org_currency, stocks_dictionary)
        value = round(value, 2)
        percentage = value / portfolio_size * 100
        percentage = round(percentage, 2)
        print("Portfelli suurus {} € - Aktsia {} väärtus {} € - Kogus {} - Portfellist {} %"
              .format(portfolio_size, sym, value, amount, percentage))


'''
stocks_portfolio_percentages(14651, fys_eur_stocks, True)
stocks_portfolio_percentages(14651, fys_usa_stocks, True)
stocks_portfolio_percentages(14651, jur_usa_stocks, True)
stocks_portfolio_percentages(14651, jur_eur_stocks, True)'''
'''
print(stock_price_from_market_watch("OLF1R", True))
print(stock_price_from_market_watch("SFG1T", True))
print(stock_price_from_market_watch("TKM1T", True))
print(stock_price_from_market_watch("EFT1T", True))
print(stock_price_from_market_watch("TSM1T", True))
print(stock_price_from_market_watch("AAPL", False))
print(stock_price_from_market_watch("TSLA", False))
print(stock_price_from_market_watch("AMD", False))
print(stock_price_from_market_watch("MSFT", False))
print(stock_price_from_market_watch("AMZN", False))'''
