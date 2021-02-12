from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Portfolio_calculator.Funcions import what_path_for_file
import xml.etree.ElementTree as ET


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

    '# List to append the XML results'
    mdlist = []
    for child in root:
        mdlist.append(child.text.strip())

    '# Make a dictionary from two lists'
    dict_list = mdlist #dict(zip(excel_headers, mdlist))
    return dict_list


print(get_vent_stats())

import pandas as pd
def to_excel(list):

    # List initialization
    list = ['Assam', 'India',
             'Lahore', 'Pakistan',
             'New York', 'USA',
             'Bejing', 'China']

    df = pd.DataFrame()

    df["<ST>"] = list[0::2]
    df["<ET>"] = list[1::2]
    df["<OT>"] = list[2::2]
    df["<WT>"] = list[3::2]
    df["<PT1>"] = list[4::2]
    df["<PT2>"] = list[5::2]
    df["<PH1>"] = list[6::2]
    df["<PH2>"] = list[7::2]
    df["<SF>"] = list[8::2]
    df["<EF>"] = list[9::2]
    df["<SP>"] = list[10::2]
    df["<EP>"] = list[11::2]
    df["<SFI>"] = list[12::2]
    df["<EFI>"] = list[13::2]
    df["<S1>"] = list[14::2]
    df["<S2>"] = list[15::2]
    df["<HE>"] = list[16::2]
    df["<WC>"] = list[17::2]
    df["<EH>"] = list[18::2]
    df["<DX>"] = list[19::2]
    df["<AD>"] = list[20::2]
    df["<FC>"] = list[21::2]
    df["<ES>"] = list[22::2]
    df["<OH>"] = list[23::2]
    df["<IH>"] = list[24::2]



    # Converting to excel
    df.to_excel(what_path_for_file() + 'result.xlsx', index=False)

to_excel(get_vent_stats())