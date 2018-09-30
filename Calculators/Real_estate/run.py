from Calculators.Real_estate import apartment_roi as roi
from Portfolio_calculator import Kinnisvara as re


'# ROI - apartment_price, down_payment_percent, other_costs, interest, loan_years, rent, monthly_insurance)'
Akad42_63 = roi.apartment_roi(re.Korter1_Hind, 20, 1500, 2.75, 15, 220, 7)
Akad38_20 = roi.apartment_roi(re.Korter2_Hind, 20, 1000, 3.7, 15, 250, 7)

'#Jooksev arvutus'
Hind = 32000
Sissemakse = 20
Kõrvalkulud = 500
Intress = 3
Laenu_aastad = 15
Üür = 240
Kindlustus = 7

new_aprt = roi.apartment_roi(Hind, Sissemakse, Kõrvalkulud, Intress, Laenu_aastad, Üür, Kindlustus)

'# name, apart_list'
roi.apart_format_print(re.Korter1_Nimi, Akad42_63)
roi.apart_format_print(re.Korter2_Nimi, Akad38_20)
roi.apart_format_print('X', new_aprt)