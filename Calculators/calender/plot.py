import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply

from Calculators.calender.gather_data import get_data_from_table

# sample data

x = get_data_from_table("Calender.db", "Kuupaevad", "Begin_date", "End_date")
y = [10, 20, 30, 40, 50, 60, 70, 80]

# data collection
trace1 = go.Scatter(x=x, y=y)

# pack the data
data = [trace1]


layout = dict(
    title='Ajatelg',
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

# plot
ply.plot(fig, filename="test.html")

