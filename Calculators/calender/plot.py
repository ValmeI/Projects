import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply

# sample data
n = 20
x = np.linspace(0, 20)
y = np.sin(x)

# data collection
trace1 = go.Scatter(x=x, y=y)

# pack the data
data = [trace1]


layout = dict(
    title='Time Series with Rangeslider',
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
            visible=True
        ),
        type='date'
    )
)

# make dictionary
fig = dict(data=data, layout=layout)

# plot
ply.plot(fig, filename="test.html")

