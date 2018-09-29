from flask import Flask, render_template

'# input pay right now (before taxes) and % that would like to work'

app = Flask(__name__)


@app.route('/')
def index():
    return "This is test"


@app.route('/work')
def work():
    return render_template("worktime.html")


if __name__ == "__main__":
    app.run(debug=True)


def work_calulator(pay, percent, hours):
    new_pay = pay * (percent/100)
    print("New pay is:", new_pay)
    new_hours = hours * (percent/100)
    print("Hours needs to work:", new_hours)


work_calulator(1250, 80, 40)
