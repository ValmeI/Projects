from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

"# removes the ====== webdriver manager ====== message from the beginning of console print out"
os.environ['WDM_LOG_LEVEL'] = '0'


def page_emails_scrape(url, page):
    options = Options()
    '# parse without displaying Chrome'
    options.add_argument("--headless")
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    '# get Chrome driver with path'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    complete_url = url + str(page)
    '# get page with url'
    driver.get(complete_url)
    '# get a list'
    data = driver.find_elements(By.PARTIAL_LINK_TEXT, "@")

    '# print emails from a list'
    for x in data:
        print(x.text)


'# run 45 times'
for i in range(1, 46):
    page_emails_scrape('https://www.hange.ee/projekteerimine/15/firmad/?page=', i)

print('All printed')

