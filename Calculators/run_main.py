# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request
from flask_wtf.csrf import CSRFProtect
from Calculators.work_time.forms import WorkForm
from Calculators.work_time.work_funcions import WorkClass as Wc

from Calculators.real_estate.form import RealEstateFrom
from Calculators.real_estate import apartment_roi as roi

from Calculators.calender.calender_form import CalenderFrom, CalenderFromDelete
from Calculators.calender.months import total

from datetime import date, timedelta
from Calculators.calender.gather_data import table_exists, create_table, insert_data, backup_to_csv, get_data_for_dropdown, delete_row
from Calculators.calender.plot import draw_plot

from Calculators.portfolio_result.portfolio_funcion import file_result_to_list, str_date_to_list
from Portfolio_calculator.Funcions import what_path_for_file
from Portfolio_calculator import Funcions

from Calculators.calender.often_used import plot_often_calender, drop_down_often_calender

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
    # 2 forms so adding dates and deleting rows would not affect each other
    form = CalenderFrom(csrf_enabled=False)
    form_1 = CalenderFromDelete(csrf_enabled=False)
    display_months = total
    table_name = "Kuupaevad"
    days_to_add = timedelta(days=28)

    if table_exists(table_name):
        pass
    else:
        create_table(table_name)
    '#plot opening the page, input needed is x1, y1, x2, y2, name of x and name of y'
    plot = plot_often_calender()

    # fill and refresh the delete drop down list
    form_1.delete_row.choices = drop_down_often_calender()

    if request.method == 'POST':

        # begin and end dates is not picked and Delete row is used/picked
        if form.beginning_date.data is None and form.end_date.data is None and form_1.delete_row.data is not None:

            # Easiest way to get values as dates for input to delete function
            for y in get_data_for_dropdown("Calender.db", "Kuupaevad", 0):
                if str(y) == form_1.delete_row.data:
                    delete_row("Calender.db", "Kuupaevad", y[0], y[1], y[2], y[3])
                    text_success = 'Kustutatud rida ' + form_1.delete_row.data
                    flash(text_success, 'success')

            '# generate again after successful post, input needed is x1, y1, x2, y2, name of x and name of y'
            plot = plot_often_calender()

            # fill and refresh the delete drop down list
            form_1.delete_row.choices = drop_down_often_calender()

            return render_template("calender.html", form=form, form_1=form_1,  display_months=display_months, plot=plot)

        # validate that end date is not same or smaller than begin date
        elif form.beginning_date.data >= form.end_date.data:
            flash('Viga: Algus kuupäev on suurem või võrdne lõpp kuupäevaga', 'danger')

        # plot a graph
        elif form.validate_on_submit():
            insert_data(table_name,
                        date.today(),
                        form.beginning_date.data, 
                        form.end_date.data, 
                        form.beginning_date.data + days_to_add,
                        form.end_date.data + days_to_add,
                        0
                        )
            new_begin = "{:%d.%m.%Y}".format(form.beginning_date.data + days_to_add)
            text_success = 'OK - Kuupäevad lisatud. Ennustatav algus kuupäev ' + new_begin
            flash(text_success, 'success')

            '# generate again after successful post, input needed is x1, y1, x2, y2, name of x and name of y'
            plot = plot_often_calender()

            '# fill and refresh the delete drop down list'
            form_1.delete_row.choices = drop_down_often_calender()

            '# backup to csv file, to prevent data loss'
            backup_to_csv("Calender.db", "Kuupaevad")

            return render_template("calender.html", form=form, form_1=form_1, display_months=display_months, plot=plot)

        else:
            flash('Sisend on vigane', 'danger')

    return render_template("calender.html", form=form, form_1=form_1, display_months=display_months, plot=plot)


"""Displays portfolio results"""


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    #path = '/volume1/Python/Calculators/portfolio_result/'
    path = what_path_for_file() + r'Calculators\portfolio_result/'
    '#input needed is x1, y1, x2, y2, name of x and name of y'
    chart_plot = draw_plot(str_date_to_list(Funcions.get_excel_column(path, "Portfell", 1)),
                           Funcions.get_excel_column(path, "Portfell", 6),
                           str_date_to_list(Funcions.get_excel_column(path, "Portfell", 1)),
                           Funcions.get_excel_column(path, "Portfell", 8),
                           'Ignar Portfell',
                           'Pere Portfell')

    portfolio_result = file_result_to_list(path, "Print_result.txt")

    return render_template("portfolio.html", portfolio_result=portfolio_result, chart_plot=chart_plot)


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
                acquired_estate = roi.format_for_page('Akadeemia 42-63', roi.apartment_roi(24500, 20, 1500, 3, 15, 220, 7, 12))
                return render_template('realestate.html', form=form, results=results, acquired_estate=acquired_estate)

            '# Selected is only Akadeemia tee 38-20'
            if form.choices.data == ['2']:
                acquired_estate = roi.format_for_page('Akadeemia 38-20', roi.apartment_roi(29900, 20, 1000, 3, 15, 260, 7, 16))
                return render_template('realestate.html', form=form, results=results, acquired_estate=acquired_estate)

            '# Both acquired apartments are selected'
            if form.choices.data == ['1', '2']:
                acquired_estate_1 = roi.format_for_page('Akadeemia 42-63', roi.apartment_roi(24500, 20, 1500, 3, 15, 220, 7, 12))
                acquired_estate_2 = roi.format_for_page('Akadeemia 38-20', roi.apartment_roi(29900, 20, 1000, 3, 15, 260, 7, 16))

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

            '# to fix floating problem in Python'
            new_pay_2 = format(new_pay[0], '.2f')
            text_success = 'Uus palganumber on ' + str(new_pay_2) + ' € ja töötunnid on ' + str(round(new_pay[1])) + 'h'
            flash(text_success, 'success')

        else:
            flash('Sisend on vigane', 'danger')
            
    return render_template("worktime.html", form=form)


if __name__ == "__main__":

    '# 0.0.0.0 = localhost and False for NAS'
    app.run(host='0.0.0.0', port=9090, debug=True)


