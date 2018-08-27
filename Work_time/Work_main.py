'# input pay right now (before taxes) and % that would like to work'


def work(pay, percent, hours):
    new_pay = pay * (percent/100)
    print("New pay is:", new_pay)
    new_hours = hours * (percent/100)
    print("Hours needs to work:", new_hours)


work(1250, 80, 40)
