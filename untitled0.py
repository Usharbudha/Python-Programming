import dash
#conda install -c anaconda dash
import dash_core_components as dcc

import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd

 

app = dash.Dash()

 

df = pd.read_csv('mpg.csv')

 

features = df.columns

 

app.layout = html.Div([

 

        html.Div([

            dcc.Dropdown(

                id='xaxis',

                options=[{'label': i.title(), 'value': i} for i in features],

                value='displacement'

            )

        ],

        style={'width': '48%', 'display': 'inline-block'}),

 

        html.Div([

            dcc.Dropdown(

                id='yaxis',

                options=[{'label': i.title(), 'value': i} for i in features],

                value='acceleration'

            )

        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

 

    dcc.Graph(id='feature-graphic')

], style={'padding':10})

 

@app.callback(Output('feature-graphic', 'figure'),[Input('xaxis', 'value'),Input('yaxis', 'value')])

def update_graph(xaxis_name, yaxis_name):

    return {

        'data': [go.Scatter(

            x=df[xaxis_name],

            y=df[yaxis_name],

            text=df['name'],

            mode='markers',

            marker={

                'size': 15,

                'opacity': 0.5,

                'line': {'width': 0.5, 'color': 'white'}

            }

        )],

        'layout': go.Layout(

            xaxis={'title': xaxis_name.title()},

            yaxis={'title': yaxis_name.title()},

            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},

            hovermode='closest'

        )

    }

 

if __name__ == '__main__':

    app.run_server()













import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

df = pd.read_csv('wheels.csv')

app.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
        value=1
    ),
    html.Div(id='wheels-output'),

    html.Hr(),  # add a horizontal rule
    dcc.RadioItems(
        id='colors',
        options=[{'label': i, 'value': i} for i in df['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-output')
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')])
def callback_a(wheels_value):
    return 'You\'ve selected "{}"'.format(wheels_value)

@app.callback(
    Output('colors-output', 'children'),
    [Input('colors', 'value')])
def callback_b(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)

if __name__ == '__main__':
    app.run_server()
    













import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64

app = dash.Dash()

df = pd.read_csv('wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
        value=1
    ),
    html.Div(id='wheels-output'),

    html.Hr(),  # add a horizontal rule
    dcc.RadioItems(
        id='colors',
        options=[{'label': i, 'value': i} for i in df['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-output'),
    html.Img(id='display-image', src='children', height=300)
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')])
def callback_a(wheels_value):
    return 'You\'ve selected "{}"'.format(wheels_value)

@app.callback(
    Output('colors-output', 'children'),
    [Input('colors', 'value')])
def callback_b(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)

@app.callback(
    Output('display-image', 'src'),
    [Input('wheels', 'value'),
     Input('colors', 'value')])
def callback_image(wheel, color):
    path = '../data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & \
    (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()














import datetime
app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:', style={'paddingRight':'30px'}),
        dcc.Input(
            id='my_ticker_symbol',
            value='TSLA', # sets a default value
            style={'fontSize':24, 'width':75}
        )
    ], style={'display':'inline-block', 'verticalAlign':'top'}),
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed = datetime(2015, 1, 1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()
        )
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])
@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_ticker_symbol', 'value'),
    Input('my_date_picker', 'start_date'),
    Input('my_date_picker', 'end_date')])
def update_graph(stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = web.DataReader(stock_ticker,'iex',start,end)
    fig = {
        'data': [
            {'x': df.index, 'y': df.close}
        ],
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()