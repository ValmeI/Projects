from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Portfolio_calculator.Funcions import what_path_for_file
import re
import time


def replace_comma_google(stat):
    '# removes comma in numbers. Is needed to convert to float. Numbers like 1,0000 and so on.'
    stat = str(stat)
    if "," in stat:
        stat = stat.replace(",", ".")
        return stat
    else:
        return stat


def replace_whitespaces(stat):
    '# removes whitespaces in numbers. Is needed to convert to float. Numbers like 1 000 and so on.'
    stat = str(stat)
    if " " in stat:
        stat = stat.replace(" ", "")
        return stat
    elif " " in stat:
        stat = stat.replace(" ", "")
        return stat
    else:
        return stat


def stock_price_from_google(stock, original_currency):

    options = Options()
    '# add options to chrome, to run it headless as not opening it'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # Bypass OS security model UPDATE 4.06.2021 problems maybe fixed it
    '# UPDATE 25.01.2021 to avoid cannot find Chrome binary error'
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
    url = "https://www.google.com/search?q=" + stock + " stock"
    driver.get(url)

    convert_html = driver.page_source
    soup = BeautifulSoup(convert_html, 'lxml')
    '# 27.01 Update, parse from google search'
    str_price_org_currency = soup.find('span', jsname='vWLAgc').text.strip(',.-').replace(' ', '')
    '# 27.01.2020 UPDATE replace comma from google'
    str_price_org_currency = replace_comma_google(str_price_org_currency)

    if original_currency:
        '#Returns original currency'
        return float(str_price_org_currency)
    else:
        '#Converts and Returns currency in euros'

        '# UPDATE 25.08.2018 USD to EUR converting page started using JS and I needed to use Selenium and Soup but'
        '# UPDATE 25.08.2018 opening every page in Chrome and parsing made it much more slower'
        '# UPDATE 14.01.2021 use Google as currency converter service'
        '# use page to convert USD to EUR'
        convert_url = "https://www.google.com/search?q=" + str_price_org_currency + "+usd+to+eur+currency+converter"
        driver.get(convert_url)
        convert_html = driver.page_source
        '# scrape with BeautifulSoup'
        soup = BeautifulSoup(convert_html, 'lxml')
        to_eur_convert = soup.find('span', class_='DFlfde SwHCTb').text
        to_eur_convert = replace_whitespaces(to_eur_convert)
        '# 27.01.2020 UPDATE replace comma from convert'
        to_eur_convert = replace_comma_google(to_eur_convert)
        '# 15.10.2021 UPDATE only keep numbers and ,.'
        to_eur_convert = re.sub("[^0-9.,]", "", to_eur_convert)
        '# UPDATE 4.06.2021 problems maybe fixed it'
        driver.quit()
        return float(to_eur_convert)


'#Stock list input and True/False as do you want it to bet original currency or in euros'


def stocks_value_combined(stock_dictionary, org_currency):
    total_value = 0
    for sym, amount in stock_dictionary.items():
        price = stock_price_from_google(sym, org_currency)
        value = price * amount
        total_value += value
    return total_value


'#Single stock price, input symbol, org_currency = True/False and stock dictionary'


def stock_amount_value(stock_symbol, org_currency, stocks_dictionary):
        amount = stocks_dictionary[stock_symbol]
        price = stock_price_from_google(stock_symbol, org_currency)
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


'# convert bitcoin to eur'

'''
def bitcoin_to_eur(var):

    options = Options()
    '# add options to chrome, to run it headless as not opening it'
    #options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # Bypass OS security model UPDATE 4.06.2021 problems maybe fixed it
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
    url = "https://www.google.com/search?q=" + str(var) + "  btc to eur"
    driver.get(url)

    convert_html = driver.page_source
    soup = BeautifulSoup(convert_html, 'lxml')
    str_price_org_currency = soup.find('span', class_='pclqee').text
    str_price_org_currency = replace_comma_google(str_price_org_currency)
    str_price_org_currency = replace_whitespaces(str_price_org_currency)
    '# UPDATE 4.06.2021 problems maybe fixed it'
    #driver.quit()
    return float(str_price_org_currency)
'''

'# UPDATE 3.09.2021: from coingecko to coinmarketcap, bc of "DDoS protection by Cloudflare"'


def crypto_price_from_coinmarketcap(coin_name):
    options = Options()
    '# add options to chrome, to run it headless as not opening it'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # Bypass OS security model UPDATE 4.06.2021 problems maybe fixed it
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
    url = "https://coinmarketcap.com/currencies/" + str(coin_name)
    driver.get(url)

    convert_html = driver.page_source
    soup = BeautifulSoup(convert_html, 'lxml')
    str_price_org_currency = soup.find('div', class_='priceValue').text.replace("$", "").replace(",", "")
    '# UPDATE 4.06.2021 problems maybe fixed it'
    driver.quit()
    return float(str_price_org_currency)


def usd_to_eur_convert(number):

    options = Options()
    '# add options to chrome, to run it headless as not opening it'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # Bypass OS security model UPDATE 4.06.2021 problems maybe fixed it
    '# UPDATE 25.01.2021 to avoid cannot find Chrome binary error'
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
    convert_url = "https://www.google.com/search?q=" + str(number) + "+usd+to+eur+currency+converter"
    driver.get(convert_url)
    convert_html = driver.page_source
    '# scrape with BeautifulSoup'
    soup = BeautifulSoup(convert_html, 'lxml')
    to_eur_convert = soup.find('span', class_='DFlfde SwHCTb').text
    to_eur_convert = replace_whitespaces(to_eur_convert)
    '# 27.01.2020 UPDATE replace comma from convert'
    to_eur_convert = replace_comma_google(to_eur_convert)
    '# 15.10.2021 UPDATE only keep numbers and ,.'
    to_eur_convert = re.sub("[^0-9.,]", "", to_eur_convert)
    '# UPDATE 4.06.2021 problems maybe fixed it'
    driver.quit()
    return float(to_eur_convert)


#print(crypto_price_from_coinmarketcap('million'))
#print(crypto_price_from_coinmarketcap('ethereum'))

#print(usd_to_eur_convert(crypto_price_from_coinmarketcap('ethereum')*0.65012))
#print(usd_to_eur_convert(crypto_price_from_coinmarketcap('bitcoin')))
#bitcoin_to_eur(0.021538)