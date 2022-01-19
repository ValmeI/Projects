
def apr_month(loan_sum, annual_interest_rate, years):
    rate = annual_interest_rate / 1200
    months = years * 12
    '# upper par'
    a = (loan_sum * rate * ((1 + rate) ** months))
    '# lower part'
    b = (((1+rate)**months)-1)
    '# dividing'
    monthly_payment = a/b

    return round(monthly_payment)


def apartment_roi(apartment_price, down_payment_percent, other_costs, interest, loan_years, rent, monthly_insurance, m2):
    '# ROI - apartment_price, down_payment_percent, other_costs, interest, loan_years, rent, monthly_insurance)'
    down_payment_amount = int(apartment_price * (down_payment_percent / 100))
    loan_amount = apartment_price - down_payment_amount
    monthly_payment = apr_month(loan_amount, interest, loan_years)
    monthly_sum = monthly_payment + monthly_insurance
    monthly_income = rent - monthly_sum
    year_income = monthly_income * 12
    cash_needed = int(down_payment_amount + other_costs)
    year_roi_percent = year_income / cash_needed * 100
    year_roi_percent = round(year_roi_percent, 1)
    m2_of_price = round(apartment_price / m2, 1)
    m2_of_rent = round(rent / m2, 1)
    return apartment_price, down_payment_amount, cash_needed, monthly_sum, monthly_income, year_income, year_roi_percent, m2_of_price, m2_of_rent


def apart_format_print(name, apart_list):
    '# for consol format'
    print('----------------------------\n'
          'Korter: {}\n'\
          'Hind: {} €\n'\
          'Laenu summa: {} €\n'\
          'Sissemakse summa: {} €\n'\
          'Esmane kulu kokku: {} €\n'\
          'Igakuine laenumakse (Kulu): {} €\n'\
          'Igakuine Üüri summa: {} €\n'\
          'Igakuine kasum (Tulu): {} €\n'\
          'Aastane kasum (Tulu): {} €\n'\
          'Ostu m2 hind: {} €/m2\n'\
          'Rendi m2 hind: {} €/m2\n'\
          '----------------------------\n'\
          'Tootlus: {} % \n\n'.format(name,
                                      apart_list[0],
                                      apart_list[0] - apart_list[1],
                                      apart_list[1],
                                      apart_list[2],
                                      apart_list[3],
                                      apart_list[3] + apart_list[4],
                                      apart_list[4],
                                      apart_list[5],
                                      apart_list[7],
                                      apart_list[8],
                                      apart_list[6]
                                      )
          )


def format_for_page(name, apart_list):

    dic_of_values = {0: 'Korter:',
                        1: 'Hind:',
                        2: 'Laenu summa:',
                        3: 'Sissemakse summa:',
                        4: 'Esmane kulu kokku:',
                        5: 'Igakuine laenumakse (Kulu):',
                        6: 'Igakuine Üüri summa:',
                        7: 'Igakuine kasum (Tulu):',
                        8: 'Aastane kasum (Tulu):',
                        9: 'Ostu m2 hind:',
                        10: 'Rendi m2 hind:',
                        11: 'Tootlus:'
                     }

    outer_list = []
    for x in range(0, len(dic_of_values)):
        inner_list = []
        if x == 0:
            inner_list.append(dic_of_values[x])
            inner_list.append(name)
            inner_list.append('-')
            outer_list.append(inner_list)

        elif x == 1:
            inner_list.append(dic_of_values[x])
            inner_list.append(apart_list[0])
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 2:
            inner_list.append(dic_of_values[x])
            inner_list.append(apart_list[0] - apart_list[1])
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 3:
            inner_list.append(dic_of_values[x])
            inner_list.append(apart_list[1])
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 4:
            inner_list.append(dic_of_values[x])
            inner_list.append(apart_list[2])
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 5:
            inner_list.append(dic_of_values[x])
            '# to fix floating problem in pyhton'
            inner_list.append(format(apart_list[3], '.2f'))
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 6:
            inner_list.append(dic_of_values[x])
            inner_list.append(apart_list[3] + apart_list[4])
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 7:
            inner_list.append(dic_of_values[x])
            '# to fix floating problem in pyhton'
            inner_list.append(format(apart_list[4], '.2f'))
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 8:
            inner_list.append(dic_of_values[x])
            '# to fix floating problem in pyhton'
            inner_list.append(format(apart_list[5], '.2f'))
            inner_list.append('€')
            outer_list.append(inner_list)

        elif x == 9:
            inner_list.append(dic_of_values[x])
            '# to fix floating problem in pyhton'
            inner_list.append(format(apart_list[7], '.2f'))
            inner_list.append('€/m2')
            outer_list.append(inner_list)

        elif x == 10:
            inner_list.append(dic_of_values[x])
            '# to fix floating problem in pyhton'
            inner_list.append(format(apart_list[8], '.2f'))
            inner_list.append('€/m2')
            outer_list.append(inner_list)

        elif x == 11:
            inner_list.append(dic_of_values[x])
            '# to fix floating problem in pyhton'
            inner_list.append(format(apart_list[6], '.2f'))
            inner_list.append('%')
            outer_list.append(inner_list)

    return outer_list


