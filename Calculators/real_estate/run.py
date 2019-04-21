from Calculators.real_estate import apartment_roi as roi
from Portfolio_calculator import Kinnisvara as Re


'# ROI - apartment_price, down_payment_percent, other_costs, interest, loan_years, rent, monthly_insurance, m2)'
Akad42_63 = roi.apartment_roi(Re.Korter1_Hind, 20, 1500, 3, 15, 220, 7, 12)
Akad38_20 = roi.apartment_roi(Re.Korter2_Hind, 20, 1000, 3, 15, 260, 7, 16)
Vilde90_193 = roi.apartment_roi(Re.Korter3_Hind, 40, 530, 2.39, 11, 230, 7, 16)

'#Jooksev arvutus'
Hind = 29500
Sissemakse = 20
Kõrvalkulud = 600
Intress = 3
Laenu_aastad = 15
Üür = 250
Kindlustus = 7
m2 = 12

new_aprt = roi.apartment_roi(Hind, Sissemakse, Kõrvalkulud, Intress, Laenu_aastad, Üür, Kindlustus, m2)

'# name, apart_list'
#roi.apart_format_print(Re.Korter1_Nimi, Akad42_63)
#roi.apart_format_print(Re.Korter2_Nimi, Akad38_20)
roi.apart_format_print('X', new_aprt)


#Akad42_63 = roi.apartment_roi(Re.Korter1_Hind, 20, 1500, 3, 15, 220, 7, 12)
#roi.format_for_page('X', Akad42_63)

