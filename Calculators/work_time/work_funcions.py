def work_calulator(pay, percent, hours):
    new_pay = pay * (percent/100)
    #print("New pay is:", new_pay)
    new_hours = hours * (percent/100)
    #print("Hours needs to work:", new_hours)
    return new_pay#, new_hours