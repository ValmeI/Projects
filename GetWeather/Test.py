from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date

url = 'http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
req = urlopen(req).read()

xml = BeautifulSoup(req, 'xml')


print('Kuupäev:', date.today())
for item in xml.findAll('station'):
    print(item)

