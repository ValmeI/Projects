import pandas as pd
import pyspark

Korter1_Nimi = "Akadeemia 42-63"
Korter2_Nimi = "Akadeemia 38-20"
Korter3_Nimi = "Vilde 90-193"

Korter1_Hind = 24500
Korter2_Hind = 29900
Korter3_Hind = 29900

Korter1_Laen = 16708.64 #Algne laen 19600
Korter2_Laen = 22146.08 #Algne laen 23920
Korter3_Laen = 17940.00

Korteri_nimed = [Korter1_Nimi, Korter2_Nimi, Korter3_Nimi]
Korteri_ostu_hind = [Korter1_Hind, Korter2_Hind, Korter3_Hind]
Korteri_laenu_summad_refinants = [Korter1_Laen, Korter2_Laen, Korter3_Laen]
Korteri_laenu_summad = [19600, 23920, Korter3_Laen]

'''
dict = {"Korter": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221]
        }
'''

list_test = [Korteri_nimed, Korteri_laenu_summad, Korteri_laenu_summad_refinants, Korteri_ostu_hind]
#print(list_test[1][0])

data = {"Korter": Korteri_nimed,
        "Laen": Korteri_laenu_summad,
        "Laen refinants": Korteri_laenu_summad_refinants,
        "Ostu hind": Korteri_ostu_hind
        }

brics = pd.DataFrame(data)

#print(brics)

from Portfolio_calculator.Funcions import update_excel

