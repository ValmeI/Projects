# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request
from flask_wtf.csrf import CSRFProtect
from Calculators.work_time.forms import WorkForm
from Calculators.work_time.work_funcions import WorkClass as Wc

from Calculators.real_estate.form import RealEstateFrom
from Calculators.real_estate import apartment_roi as roi

from Calculators.calender.calender_form import CalenderFrom
from Calculators.calender.months import total

from datetime import date
from Calculators.calender.gather_data import table_exists, create_table, insert_data

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)

app.config['SECRET_KEY'] = 'secret'

"""index html"""


@app.route('/')
def index():
    return render_template("index.html")


"""calender part of page"""


@app.route('/calender', methods=['GET', 'POST'])
def calender():
    # TODO kuna ei tööta kui true, ei tea miks
    form = CalenderFrom(csrf_enabled=False)
    display_months = total
    table_name = "Kuupaevad"

    if table_exists(table_name):
        pass
    else:
        create_table(table_name)

    if request.method == 'POST':

        '# validate that end date is not same or smaller than begin date'
        if form.beginning_date.data >= form.end_date.data:
            flash('Viga: Algus kuupäev on suurem või võrdne lõpp kuupäevaga', 'danger')

        elif form.validate_on_submit():
            insert_data(date.today(), form.beginning_date.data, form.end_date.data, table_name)

            flash('Sisestus oli eduakas, kuupäevad lisatud', 'success')

        else:
            flash('Sisend on vigane', 'danger')

    return render_template("calender.html", form=form, display_months=display_months)


"""real estate part of the page"""


@app.route('/real_estate', methods=['GET', 'POST'])
def real_estate():
    # TODO kuna ei tööta kui true, ei tea miks
    form = RealEstateFrom(csrf_enabled=False, )

    if request.method == 'POST':
        if form.validate_on_submit():

            '#results = request.form #dont know why it is needed or not needed'

            new_aprt = roi.apartment_roi(form.price.data,
                                         form.finance.data,
                                         form.side_costs.data,
                                         form.rate.data,
                                         form.period.data,
                                         form.rent_per_month.data,
                                         form.insurance.data,
                                         form.m2.data)

            flash('Arvutatud', 'success')

            results = roi.format_for_page('Aadress X', new_aprt)

            '# Selected is only Akadeemia tee 42-63'
            if form.choices.data == ['1']:
                acquired_estate = roi.format_for_page('Akadeemia 42-63',
                                                      roi.apartment_roi(24500, 20, 1500, 3, 15, 220, 7, 12))
                return render_template('realestate.html', form=form, results=results, acquired_estate=acquired_estate)

            '# Selected is only Akadeemia tee 38-20'
            if form.choices.data == ['2']:
                acquired_estate = roi.format_for_page('Akadeemia 38-20',
                                                  roi.apartment_roi(29900, 20, 1000, 3, 15, 260, 7, 16))
                return render_template('realestate.html', form=form, results=results, acquired_estate=acquired_estate)

            '# Both acquired apartments are selected'
            if form.choices.data == ['1', '2']:
                acquired_estate_1 = roi.format_for_page('Akadeemia 42-63',
                                                      roi.apartment_roi(24500, 20, 1500, 3, 15, 220, 7, 12))
                acquired_estate_2 = roi.format_for_page('Akadeemia 38-20',
                                                      roi.apartment_roi(29900, 20, 1000, 3, 15, 260, 7, 16))

                return render_template('realestate.html', form=form, results=results, acquired_estate=acquired_estate_1,
                                       acquired_estate2=acquired_estate_2)

            else:
                return render_template('realestate.html', form=form, results=results)

        else:
            flash('Sisend on vigane', 'danger')

    return render_template("realestate.html", form=form)


"""work time part of page"""


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

            new_pay = Wc.work_calulator(form.pay.data, new_percent)
            '# to fix floating problem in pyhton'
            new_pay_2 = format(new_pay[0], '.2f')
            text_success = 'Uus palganumber on ' + str(new_pay_2) + ' € ja töötunnid on ' + str(round(new_pay[1])) + 'h'
            flash(text_success, 'success')

        else:
            flash('Sisend on vigane', 'danger')
            
    return render_template("worktime.html", form=form)


if __name__ == "__main__":

    '# 0.0.0.0 = localhost'
    app.run(host='0.0.0.0', port=9090, debug=True)


