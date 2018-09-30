from Portfolio_calculator import Kinnisvara as re


def apartment_roi(apartment_price, down_payment_percent, other_costs, interest, loan_years, rent, monthly_insurance):
    '# ROI - apartment_price, down_payment_percent, other_costs, interest, loan_years, rent, monthly_insurance)'
    down_payment_amount = int(apartment_price * (down_payment_percent / 100))
    loan_amount = apartment_price - down_payment_amount
    monthly_payment = re.apr_month(loan_amount, interest, loan_years)
    monthly_sum = monthly_payment + monthly_insurance
    monthly_income = rent - monthly_sum
    year_income = monthly_income * 12
    cash_needed = int(down_payment_amount + other_costs)
    year_roi_percent = year_income / cash_needed * 100
    year_roi_percent = round(year_roi_percent, 1)
    return apartment_price, down_payment_amount, cash_needed, monthly_sum, monthly_income, year_income, year_roi_percent


def apart_format_print(name, apart_list):
    print('----------------------------\n'
          'Korter: {}\n'
          'Hind: {} €\n'
          'Laenu summa: {} €\n'
          'Sissemakse summa: {} €\n'
          'Esmane kulu kokku: {} €\n'
          'Igakuine laenumakse (Kulu): {} €\n'
          'Igakuine Üüri summa: {} €\n'
          'Igakuine kasum (Tulu): {} €\n'
          'Aastane kasum (Tulu): {} €\n'
          '----------------------------\n'
          'Tootlus: {} % \n\n'.format(name,
                                      apart_list[0],
                                      apart_list[0] - apart_list[1],
                                      apart_list[1],
                                      apart_list[2],
                                      apart_list[3],
                                      apart_list[3] + apart_list[4],
                                      apart_list[4],
                                      apart_list[5],
                                      apart_list[6])
          )


'''
Akad42_63 = apartment_roi(re.Korter1_Hind, 20, 1500, 2.75, 15, 220, 7)
print(Akad42_63)
apart_format_print('X', Akad42_63)
'''