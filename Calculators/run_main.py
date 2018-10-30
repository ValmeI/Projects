# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request
from Calculators.work_time.forms import WorkForm
from flask_wtf.csrf import CSRFProtect
from Calculators.work_time.work_funcions import WorkClass as WC


csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)

app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/work', methods=['GET', 'POST'])
def work():
    # TODO kuna ei tööta kui true, ei tea miks
    form = WorkForm(csrf_enabled=False)

    if request.method == 'POST':
        if form.validate_on_submit():
            '# so 0.8 and so on is also accepted input'
            if form.percent.data < 1:

                new_percent = form.percent.data * 100
            else:
                new_percent = form.percent.data

            new_pay = WC.work_calulator(form.pay.data, new_percent)
            '# to fix floating problem in pyhton'
            new_pay_2 = format(new_pay[0], '.2f')
            text_success = 'Uus palganumber on ' + str(new_pay_2) + ' € ja töötunnid on ' + str(round(new_pay[1])) + 'h'
            flash(text_success, 'success')

        else:
            flash('Sisend on vigane', 'danger')
            
    return render_template("worktime.html", form=form)


if __name__ == "__main__":

    '# 0.0.0.0 = localhost'
    app.run(host='0.0.0.0', port=9090)#, debug=True)


