from dateutil import relativedelta
from xlwt import Workbook
from xlutils.copy import copy
from datetime import date
import xlrd
import os.path

'# Funderbean imports'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json


'# get today'
today_str = str(date.today())
'# how much extend excel columns'
column_extender = 350

'#kodu path'
path_home = r"D:\PycharmProjects\Projects/"

'#Laptop path'
path_laptop = r"C:\PycharmProjects/"

'#töö path'
path_work = r"V:\rik_oigusk\Päringud\Krmr\Ignar Valme\PythonProjects\Projects/"

'# headrid mida exceli loogmisel ja updateimisel kasutatakse'
headers = {0: "Kuupäev",
           1: "Kinnisvara puhas väärtus",
           2: "Füüsilise isiku aktsiad",
           3: "Juriidilise isiku aktsiad",
           4: "Aktsiad kokku",
           5: "Terve portfell kokku",
           6: "Mörr-i portfell",
           7: "Pere portfell kokku",
           8: "Vilde after Tax",
           9: "Vaba Raha",
           10: "Funderbeam Väärtus"}


def vilde_calculation(input_day, last_calculation_sum, new_sum_to_add, last_input_excel_date):
    if date.today().day == input_day and str(date.today()) != last_input_excel_date:
        new_vilde = float(last_calculation_sum)
        new_vilde += float(new_sum_to_add)
        return new_vilde
    else:
        return float(last_calculation_sum)


def dividend_with_certain_date(sum):
    after_tax = sum - (sum * 0.2)
    return after_tax


def what_path_for_file():
    if os.path.exists(path_home):
        return str(path_home)

    elif os.path.exists(path_work):
        return str(path_work)

    elif os.path.exists(path_laptop):
        return str(path_laptop)


def diff_months(date2, date1):
    '#saada, et palju on tänase ja laenu kuupäevade vahe'
    difference = relativedelta.relativedelta(date2, date1)
    '#konventeerida aastad kuudeks ja liita leitud kuud'
    total_months = difference.years*12+difference.months
    return total_months


def freeze_excel_rows(variable, horz_pos, vert_pos):
    '# freeze excel rows'
    variable.set_panes_frozen(True)
    variable.set_horz_split_pos(horz_pos)
    variable.set_vert_split_pos(vert_pos)


def create_excel(excel_name, sheet_name):

    wb = Workbook()
    sheet1 = wb.add_sheet(sheet_name)

    'freeze rows'
    freeze_excel_rows(sheet1, 1, 1)

    '#lisab file type'
    file_name = excel_name + ".xls"

    for column, value in headers.items():
        '# row=0, column and value'
        sheet1.write(0, column, value)
        sheet1.col(column).width = len(value*column_extender)

    '#salvestab exceli'
    wb.save(file_name)

    print("========================")
    print("Loodud uus fail", file_name)


'#tuleb sisse anda ka faili nimi, kontrollib kahjuks ainult kodu arvutit'


def check_if_excel_exists(excel_name):

    '#kodu path ja töö path viidud muutujasse'
    if os.path.isfile(what_path_for_file() + 'Portfolio_calculator/' + excel_name + ".xls"):
        return True
    else:
        return False


'#kontroll kas ülemine faili kontroll tagastab, et fail olemas, kui ei siis käivitab üleval oleval exceli faili loomise'


def need_new_excel_file(excel_name, sheet_name):
    if check_if_excel_exists(excel_name):
        print("========================")
        print("Fail juba kaustas olemas.")
    else:
        create_excel(excel_name, sheet_name)


def update_excel(path, excel_name, kinnisvara_puhas, füs_aktsiad, jur_aktsiad,
                 aktsiad_kokku, kokku_portfell, abikaasa_kokku,
                 pere_kokku, vildeAfterTax, vabaRaha, FunderbeamValue, laps_kokku):
    '# add file type'
    file_name = excel_name + ".xls"
    '#open excel file'
    rb = xlrd.open_workbook(path + file_name)
    '#make a writeable copy'
    copy_rb = copy(rb)
    '#take the first sheet from excel'
    w_sheet = copy_rb.get_sheet(0)

    'freeze rows'
    freeze_excel_rows(w_sheet, 1, 1)

    '# Indekis järgi võtab open_workbooki esimeses sheeti, vajaduse et kontrolida clowum ja row väärtusi'
    first_sheet = rb.sheet_by_index(0)

    '# Et updateiga ei läheks iga kord headeri suurused kaduma ehk need tuleb iga kord uuesti suureks teha'
    for column, value in headers.items():
        '# row=0, column and value'
        w_sheet.write(0, column, value)
        w_sheet.col(column).width = len(value*column_extender)

    '#column 0 ehk kus alustada'
    c = 0
    value = 0
    max_rows = first_sheet.nrows
    '#kui see saab õige nr siis kontrolli läbinud'
    passed = 0

    '# käib läbi rea väärtused (-1 vajalik, et saada täidetud väärtused)'
    for check in first_sheet.row_values(max_rows-1):
        if check == today_str:
            passed += 1
        elif check == kinnisvara_puhas:
            passed += 1
        elif check == füs_aktsiad:
            passed += 1
        elif check == jur_aktsiad:
            passed += 1
        elif check == aktsiad_kokku:
            passed += 1
        elif check == kokku_portfell:
            passed += 1
        elif check == abikaasa_kokku:
            passed += 1
        elif check == pere_kokku:
            passed += 1
        elif check == vildeAfterTax:
            passed += 1
        elif check == vabaRaha:
            passed += 1
        elif check == FunderbeamValue:
            passed += 1
        elif check == laps_kokku:
            passed += 1

    '#ehk 8 kontrolli on. Sama palju kui välju. Kui andmed muutunud siis lisab need, kui ei väljastab lause, et ei ole muutunud'
    if passed == first_sheet.ncols:
        print("Tänase päeva andmed pole muutunud.")

        '# get cell of pervious row date value, input (rows, col). If date is same then update same row, to avoid multiple same date rows '
    elif first_sheet.cell(max_rows - 1, 0).value == today_str:
        while c < first_sheet.ncols:
            if c == 0:
                value = today_str
            elif c == 1:
                value = kinnisvara_puhas
            elif c == 2:
                value = füs_aktsiad
            elif c == 3:
                value = jur_aktsiad
            elif c == 4:
                value = aktsiad_kokku
            elif c == 5:
                value = kokku_portfell
            elif c == 6:
                value = abikaasa_kokku
            elif c == 7:
                value = pere_kokku
            elif c == 8:
                value = vildeAfterTax
            elif c == 9:
                value = vabaRaha
            elif c == 10:
                value = FunderbeamValue
            elif c == 11:
                value = laps_kokku

            '# row-1( to get previous row), column ja tekst'
            w_sheet.write(max_rows - 1, c, value)
            c += 1
        copy_rb.save(file_name)
        print("Tänane seis muudetud.")

    else:
        '# Et me ei läheks indeksist välja muidu tuleb veateade ning täitmaks selle päeva portfelli seisu'
        while c < first_sheet.ncols:
            if c == 0:
                value = today_str
            elif c == 1:
                value = kinnisvara_puhas
            elif c == 2:
                value = füs_aktsiad
            elif c == 3:
                value = jur_aktsiad
            elif c == 4:
                value = aktsiad_kokku
            elif c == 5:
                value = kokku_portfell
            elif c == 6:
                value = abikaasa_kokku
            elif c == 7:
                value = pere_kokku
            elif c == 8:
                value = vildeAfterTax
            elif c == 9:
                value = vabaRaha
            elif c == 10:
                value = FunderbeamValue
            elif c == 11:
                value = laps_kokku

            '# last row, column ja tekst'
            w_sheet.write(max_rows, c, value)
            c += 1
        copy_rb.save(file_name)
        print("Tänane seis lisatud.")


def get_excel_column(path, excel_name, column_number):
    column_list = []
    '# Kergem anda sisendisse 1 tulp ning hiljem -1 teha kuna lugemine hakkab 0ist'
    column_number = column_number-1
    '# lisab file type'
    file_name = excel_name + ".xls"
    '# open excel file'
    rb = xlrd.open_workbook(path + file_name)
    first_sheet = rb.sheet_by_index(0)

    for col in first_sheet.col_values(column_number):
        '# kõik string siis ei tule errorit, vajadus et header ei tuleks listi'
        if str(col) in headers.get(column_number):
            continue
        column_list.append(col)
    return column_list


def get_last_row(path, excel_name, column_number):

    '# Kergem anda sisendisse 1 tulp ning hiljem -1 teha kuna lugemine hakkab 0ist'
    column_number = column_number - 1
    '# lisab file type'
    file_name = excel_name + ".xls"
    '# open excel file'
    rb = xlrd.open_workbook(path + file_name)
    first_sheet = rb.sheet_by_index(0)

    max_rows = first_sheet.nrows

    '# to get only that column number that was wanted in function input, enumerate counts'
    for column, max_value in enumerate(first_sheet.row_values(max_rows-1)):
        '# if column_number form function input is the same as in loop return that max'
        if column == column_number:

            return max_value


'# get funderbeam_marketvalue'


def get_funderbeam_marketvalue():
    options = Options()
    '# parse without displaying Chrome'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')  # Bypass OS security model UPDATE 4.06.2021 problems maybe fixed it
    '# UPDATE 25.01.2021 to avoid cannot find Chrome binary error'
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
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
        '# Sleep so it could load role selection page, UPDATE: 21.04.2021 Before it was 1 sleep time, Funderbeam might have perf problems'
        time.sleep(5)
        '# Select element nr 1, as nr 0 is personal role and nr 1 is company role. Need company role'
        driver.find_elements_by_class_name('cards__title')[1].click()
        '# Sleep so it could load company dashboard, UPDATE: 21.04.2021 Before it was 1 sleep time, Funderbeam might have perf problems'
        time.sleep(5)
        '# get data from direct url API'
        data = driver.get('https://www.funderbeam.com/api/user/tokenSummaryStatement')
        '# get page source'
        driver.page_source
        '# parse only json part of the page source'
        content = driver.find_element_by_tag_name('pre').text
        parsed_json = json.loads(content)
        '# to get only marketValueTotal'
        parsed_market_value = parsed_json['totals'][0]['marketValueTotal']
        '# UPDATE 4.06.2021 problems maybe fixed it'
        driver.quit()

        return parsed_market_value
