from xlutils.copy import copy
import xlrd
import csv

excel_name = 'Vihik1'
excel_name_import = 'Import tulemused'

file_name = excel_name + ".xlsx"
'#open excel file'
rb = xlrd.open_workbook(file_name)
'#make a writeable copy'
copy_rb = copy(rb)
'#take the first sheet from excel'
w_sheet = copy_rb.get_sheet(0)
'# Indekis järgi võtab open_workbooki esimeses sheeti, vajaduse et kontrolida clowum ja row väärtusi'
first_sheet = rb.sheet_by_index(0)
'# max rows ehk teada kui kaua loompime'
max_rows = first_sheet.nrows
'# Kui palju ridu tuleb kirjutada'
max_ros_write = 0
ÄR_list = []

for x in range(0, max_rows):
    '# kui ÄN ehk ärinõue siis võta tagasta'
    if 'ÄN-' in first_sheet.row_values(x)[0]:
        #print(first_sheet.row_values(x)[0])
        value = first_sheet.row_values(x)[0]
        '#Kui leiame mida kirjutada siis lisame row counti juurde +1'
        max_ros_write += 1
        ÄR_list.append(value)

#print(max_ros_write)
#print(ÄR_list)

row = 0

with open('Import tulemused.csv', mode='w', newline='') as ÄR_file:
    ÄR_writer = csv.writer(ÄR_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, )

    for y in ÄR_list:
        ÄR_writer.writerow([y])
        #print(row, 0, y)
        row += 1
print("Excel Import loodud")




