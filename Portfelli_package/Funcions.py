from dateutil import relativedelta
from xlwt import Workbook
from xlutils.copy import copy
from datetime import date
import xlrd
import os.path

'# get today'
today_str = str(date.today())
'# how much extend excel columns'
column_extender = 350
'#kodu path'
excel_path_home = r"D:\PycharmProjects\Projects\Portfelli_package/" \

'#töö path'
excel_path_work = r"V:\rik_oigusk\Päringud\Krmr\Ignar Valme\PythonProjects\Portfelli_package/"

'# headrid mida exceli loogmisel ja updateimisel kasutatakse'
headers = {0: "Kuupäev",
           1: "Kinnisvara puhas väärtus",
           2: "Füüsilise isiku aktsiad",
           3: "Juriidilise isiku aktsiad",
           4: "Aktsiad kokku",
           5: "Terve portfell kokku"}


def what_path_for_excel():
    if os.path.exists(excel_path_home):

        return excel_path_home
    elif os.path.exists(excel_path_work):

        return excel_path_work


def diff_months(date2, date1):
    '#saada, et palju on tänase ja laenu kuupäevade vahe'
    difference = relativedelta.relativedelta(date2, date1)
    '#konventeerida aastad kuudeks ja liita leitud kuud'
    total_months = difference.years*12+difference.months
    return total_months


def create_excel(excel_name):

    wb = Workbook()
    sheet1 = wb.add_sheet("Porfelli Info")
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
    if os.path.isfile(what_path_for_excel() + excel_name + ".xls"):
        return True
    else:
        return False


'#kontroll kas ülemine faili kontroll tagastab, et fail olemas, kui ei siis käivitab üleval oleval exceli faili loomise'


def need_new_excel_file(excel_name):
    if check_if_excel_exists(excel_name):
        print("========================")
        print("Fail juba kaustas olemas.")
    else:
        create_excel(excel_name)


def update_excel(excel_name, kinnisvara_puhas, füs_aktsiad, jur_aktsiad, aktsiad_kokku, kokku_portfell):
    '# add file type'
    file_name = excel_name + ".xls"
    '#open excel file'
    rb = xlrd.open_workbook(file_name)
    '#make a writeable copy'
    copy_rb = copy(rb)
    '#take the first sheet from excel'
    w_sheet = copy_rb.get_sheet(0)

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

    '#ehk 6 kontrolli on. Sama palju kui välju. Kui andmed muutunud siis lisab need, kui ei väljastab lause, et ei ole muutunud'
    if passed == first_sheet.ncols:
        print("Tänase päeva andmed pole muutunud.")
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

            '# row, column ja tekst'
            w_sheet.write(max_rows, c, value)
            c += 1
        copy_rb.save(file_name)
        print("Tänane seis lisatud.")


def get_excel_column(excel_name, column_number):
    column_list = []
    '# Kergem anda sisendisse 1 tulp ning hiljem -1 teha kuna lugemine hakkab 0ist'
    column_number = column_number-1
    '# lisab file type'
    file_name = excel_name + ".xls"
    '# open excel file'
    rb = xlrd.open_workbook(file_name)
    first_sheet = rb.sheet_by_index(0)

    for col in first_sheet.col_values(column_number):
        '# kõik string siis ei tule errorit, vajadus et header ei tuleks listi'
        if str(col) in headers.get(column_number):
            continue
        column_list.append(col)
    return column_list


def get_last_row(excel_name, column_number):

    '# Kergem anda sisendisse 1 tulp ning hiljem -1 teha kuna lugemine hakkab 0ist'
    column_number = column_number - 1
    '# lisab file type'
    file_name = excel_name + ".xls"
    '# open excel file'
    rb = xlrd.open_workbook(file_name)
    first_sheet = rb.sheet_by_index(0)

    max_rows = first_sheet.nrows

    '# to get only that column number that was wanted in function input, enumerate counts'
    for column, max_value in enumerate(first_sheet.row_values(max_rows-1)):
        '# if column_number form function input is the same as in loop return that max'
        if column == column_number:

            return max_value

