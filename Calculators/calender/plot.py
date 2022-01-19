import plotly.graph_objs as go
import plotly.offline as ply
from Calculators-Website-Flask.calender.gather_data import get_data_from_table, create_fictitious_dates


def draw_plot(input_x1, input_y1, input_x2, input_y2, scatter_name1, scatter_name2):
    # only dates
    x = input_x1
    # only values
    y = input_y1

    # only dates
    x2 = input_x2
    # only values
    y2 = input_y2

    # data collection
    trace1 = go.Scatter(x=x, y=y, name=scatter_name1)
    trace2 = go.Scatter(x=x2, y=y2, name=scatter_name2)

    # pack the data
    data = [trace1, trace2]

    layout = dict(
        title='Chart',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=3,
                         label='3m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=False
            ),
            type='date'
        )
    )

    # make dictionary
    fig = dict(data=data, layout=layout)
    # div returns text as html
    return ply.plot(fig, output_type='div')

'''
# only dates
x1 = create_fictitious_dates(get_data_from_table("Calender.db", "Kuupaevad", "Begin_date", "End_date"))[0]
# only values
y1 = create_fictitious_dates(get_data_from_table("Calender.db", "Kuupaevad", "Begin_date", "End_date"))[1]
x2 = create_fictitious_dates(get_data_from_table("Calender.db", "Kuupaevad", "Predict_begin_date", "Predict_end_date"))[0]
y2 = create_fictitious_dates(get_data_from_table("Calender.db", "Kuupaevad", "Predict_begin_date", "Predict_end_date"))[1]

draw_plot(x1, y1, x2, y2)
'''
