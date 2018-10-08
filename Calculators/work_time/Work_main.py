from flask import Flask, render_template, flash
from Calculators.work_time.forms import WorkForm

'# input pay right now (before taxes) and % that would like to work'

app = Flask(__name__)

app.config['SECRET_KEY'] = '111111'


@app.route('/')
def index():
    return "This is test"


@app.route('/work', methods=['GET', 'POST'])
def work():
    form = WorkForm()

    return render_template("worktime.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

'''
def work_calulator(pay, percent, hours):
    new_pay = pay * (percent/100)
    print("New pay is:", new_pay)
    new_hours = hours * (percent/100)
    print("Hours needs to work:", new_hours)


work_calulator(1250, 80, 40)
'''