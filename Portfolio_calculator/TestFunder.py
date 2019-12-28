from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Portfolio_calculator.Funcions import what_path_for_file
from selenium.webdriver.common.keys import Keys  # need to send keystrokes

options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
url = "https://www.funderbeam.com/dashboard"
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
    driver.find_element_by_class_name('button-primary').send_keys("\n") #send enter for links, buttons
    driver.implicitly_wait(100)

    test = driver.find_element_by_link_text('Valix Invest').click()
    driver.find_element_by_link_text('Valix Invest').send_keys("\n")
    print(test)