from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

# chained callback

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

layout = html.Div([
    html.Label("Group Managers", id='label'),
    dcc.Input(value='MTL', type='text', id='input'),
    html.Div("Result of Input", id='element'),
    html.Div("Result of Input", id='element2'),

    html.Label("City option", id='label-city'),
    dcc.RadioItems(id="city-radio",
                   options=[{'label': item, 'value': item} for item in all_options.keys()]),
    html.Label("District option", id='label-district'),
    dcc.RadioItems(id="district-radio"),
    html.Div(id='display-values')
])


@app.callback(
    Output('element', 'children'),
    Input('input', 'value')
)
def get_result(value):
    return "element covered " + value


@app.callback(
    Output('element2', 'children'),
    Input('element', 'children')
)
def get_result(value):
    return "element2 get: " + value


@app.callback(
    Output('district-radio', 'options'),
    Input('city-radio', 'value')
)
def get_result(value):
    print("==== value ", value)

    if value not in all_options.keys():
        return []
    print("==== value ", value)
    return [{'label': item, 'value': item} for item in all_options[value]]
