from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Portfolio_calculator.Funcions import what_path_for_file
import xml.etree.ElementTree as ET


def get_vent_stats():
    options = Options()
    '# parse without displaying Chrome'
    options.add_argument("--headless")
    '# UPDATE 25.01.2021 to avoid cannot find Chrome binary error'
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    '# get Chrome driver with path'
    driver = webdriver.Chrome(what_path_for_file() + "chromedriver.exe", options=options)
    '# url we want to parse: Komfovent local IP'
    url = "http://192.168.1.60/"
    '# get url'
    driver.get(url)

    '# If KONTROLL and so on elements are not found go and log in, '
    ' if they are found then we are still logged in (previous session is still active) '
    'and skip the login part and go straight to API'
    if len(driver.find_elements_by_class_name('name')):
        pass
    else:
        driver.find_element_by_id('i_p').send_keys('user')
        driver.find_element_by_id('b_s').submit()

    '# get data from direct url API'
    driver.get('http://192.168.1.60/det.asp')
    '# get page source'
    data = driver.page_source
    '# Get XML part of the source'
    content = driver.find_element_by_id('webkit-xml-viewer-source-xml').get_attribute("innerHTML")
    '# Make page source string to XML'
    tree = ET.ElementTree(ET.fromstring(content))
    '# Get root of xml for the loop'
    root = tree.getroot()

    '# Excel headers'
    excel_headers = ["Sissepuhke temperatuur",
                     "Väljatõmbe temperatuur",
                     "Välistemperatuur",
                     "Paneeli temperatuur",
                     "Paneeli niiskus RH",
                     "SP ventilaator",
                     "VT ventilaator",
                     "Soojusvaheti",
                     "El. Kalorifeer",
                     "Õhuklappid",
                     "Filteri ummistumine",
                     "Energiasääst"
                     "Ruumi niiskus AH"]  # all keys to be extracted from xml

    '# List to append the XML results'
    mdlist = []
    for child in root:
        mdlist.append(child.text.strip())
    return print(excel_headers, '\n\n', mdlist)


get_vent_stats()

