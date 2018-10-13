def work_calulator(pay, percent):
    default_h = 40
    new_pay = pay * (percent/100)
    new_hours = default_h * (percent/100)
    return new_pay, new_hours
