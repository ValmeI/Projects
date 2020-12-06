from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Portfolio_calculator.Funcions import what_path_for_file
import time
import json

options = Options()
'# parse without displaying Chrome'
options.add_argument("--headless")
'# get Chrome driver with path'
driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
'# url we want to parse'
url = "https://www.funderbeam.com/dashboard"
'# get url'
driver.get(url)

'# Pass file name'
password_file = 'FunderPass'

'# get password form file, read only'
open_file = open(password_file + ".txt", 'r')
for password in open_file:
    '# send username'
    driver.find_element_by_name('username').send_keys('ignarvalme@gmail.com')
    '# send password'
    driver.find_element_by_name('password').send_keys(password)
    '#send enter for links, buttons'
    driver.find_element_by_class_name('button-primary').send_keys("\n")
    '# Sleep so it could load role selection page'
    time.sleep(1)
    '# Select element nr 1, as nr 0 is personal role and nr 1 is company role. Need company role'
    driver.find_elements_by_class_name('cards__title')[1].click()
    '# Sleep so it could load company dashboard'
    time.sleep(1)
    '# get data from direct url API'
    data = driver.get('https://www.funderbeam.com/api/user/tokenSummaryStatement')
    '# get page source'
    driver.page_source
    '# parse only json part of the page source'
    content = driver.find_element_by_tag_name('pre').text
    parsed_json = json.loads(content)
    '# to get only marketValueTotal'
    print(parsed_json['totals'][0]['marketValueTotal'])

