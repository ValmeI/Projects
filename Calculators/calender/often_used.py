from Calculators-Website-Flask.calender.plot import draw_plot
from Calculators-Website-Flask.calender.gather_data import create_fictitious_dates, get_data_from_table, get_data_for_dropdown
from Calculators-Website-Flask.calender.calender_form import CalenderFromDelete
from dateutil.parser import parse


def plot_often_calender():

    get_actual_data = get_data_from_table("Calender.db", "Kuupaevad", "Begin_date", "End_date", 0)
    get_predict_data = get_data_from_table("Calender.db", "Kuupaevad", "Predict_begin_date", "Predict_end_date", 0)

    often_plot = draw_plot(
                    create_fictitious_dates(get_actual_data)[0],
                    create_fictitious_dates(get_actual_data)[1],
                    create_fictitious_dates(get_predict_data)[0],
                    create_fictitious_dates(get_predict_data)[1],
                    'Actual Dates',
                    'Predictable Dates'
                    )

    return often_plot


def drop_down_often_calender():
    # Clear the SelectField on page load and add choices form database
    form_1 = CalenderFromDelete(csrf_enabled=False)
    form_1.delete_row.choices = []
    # Empty choices added every time
    form_1.delete_row.choices += [('', '')]
    for row in get_data_for_dropdown("Calender.db", "Kuupaevad", 0):

        # parse to date and then format to dd.mm.yy
        new_row0 = "{:%d.%m.%Y}".format(parse(row[0]))
        new_row1 = "{:%d.%m.%Y}".format(parse(row[1]))
        new_row2 = "{:%d.%m.%Y}".format(parse(row[2]))
        new_row3 = "{:%d.%m.%Y}".format(parse(row[3]))

        form_1.delete_row.choices += [(row, 'Begin: ' + new_row0 +
                                       ' End: ' + new_row1 +
                                       ' Predict Begin: ' + new_row2 +
                                       ' Predict End: ' + new_row3
                                       )]
    return form_1.delete_row.choices


