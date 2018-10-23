# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request
from Calculators.forms import WorkForm
from flask_wtf.csrf import CSRFProtect
from Calculators.work_time import work_funcions as wf
import Calculators

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

            new_pay = wf.work_calulator(form.pay.data, new_percent)
            flash(f'Uus palganumber on { new_pay[0] } € ja töötunnid on { round(new_pay[1]) }h', 'success')

        else:
            flash('Sisend on vigane', 'danger')
            
    return render_template("worktime.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)


