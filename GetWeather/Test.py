from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date

url = 'http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
req = urlopen(req).read()

xml = BeautifulSoup(req, 'xml', from_encoding='utf8')


print('Kuupäev:', date.today())
list_proov = [['name'
,'wmocode'
,'longitude'
,'latitude'
,'phenomenon'
,'visibility'
,'precipitations'
,'airpressure'
,'relativehumidity'
,'airtemperature'
,'winddirection'
,'windspeed'
,'windspeedmax'
,'waterlevel'
,'waterlevel_eh2000'
,'watertemperature'
,'uvindex']]
for item in xml.findAll('station'):
    #list_proov.append(item.text)
    print(item.find('wmocode'))
    print(type(item.find('wmocode')))
#print(list_proov)

