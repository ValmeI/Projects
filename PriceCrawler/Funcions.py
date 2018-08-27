from lxml import html
import requests
from bs4 import BeautifulSoup


product = "mx master"
url = "https://www.hagglezon.com/en/s/" + product
name_length = 2
list_length = 10

page = requests.get(url)
tree = html.fromstring(page.content)
plain_text = page.text
soup = BeautifulSoup(plain_text, "html.parser")

names = []
prices = []
links = []

for name in soup.findAll('div', {'class': 'LinesEllipsis '}):
    string_name = name.contents[0] # Ei ole string vaid on tag, ei tea mis moodi tuvastada, äkki print type?
    if len(names) < name_length:
        names.append(string_name)


for price in soup.findAll('span', {'class': 'priceValue-3EL-ZvhYipeqU8SZXKZAAO'}):
    string_price = price.string
    if len(prices) < list_length:
        prices.append(string_price)

for link in soup.findAll('a', {'class': 'buyButton-1EdpR5Suc8oyGCKa72Es0h'}):
    href_link = link.get('href')
    if len(links) < list_length:
        links.append(href_link)

'''print(names)
print(prices)
print(links)'''



total = []
for price2, link2 in zip(prices, links):
    print(price2, link2)