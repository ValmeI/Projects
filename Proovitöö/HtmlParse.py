import pandas as pd
import re

url = 'https://www.xdream.ee/tul/koondtabel_2010.html'

'# Returns list of all tables on page'
tables = pd.read_html(url)
'# Select table of interest'
result_df = tables[1]
'# Replace Nan with NULL for database'
result_df = result_df.fillna('NULL')
'# Get year nr from url'
Calender_year = re.sub(r"\D", "", url)

for index, row in result_df.iterrows():

    '# skip tables column names as insert Values'
    if index == 0:
        continue

    print("INSERT INTO Tulemused_{} "
          "([Koht],[Nimi],[Liikmed],[Rada],[Punktid],[{}],[{}],[{}],[{}]) "
          "values({},'{}','{}','{}',{},{},{},{},{})".format(
            int(Calender_year), #urlist aasta
            result_df[5][0], #value Saku
            result_df[6][0], #value Tamsalu
            result_df[7][0], #value Karula
            result_df[8][0], #value Roosta
            row[0],#Koht
            row[1],#Nimi
            row[2],#Liikmed
            row[3],#Rada
            row[4],#Punktid
            row[5],#punktid Saku
            row[6],#punktid Tamsalu
            row[7],#punktid Karula
            row[8] #punktid Roosta
             )
         )

print( )
