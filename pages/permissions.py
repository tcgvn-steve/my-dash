from dash import dcc
import dash_html_components as html
from app import app
from dash.dependencies import Input, Output, State

layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(
    Output('output-state', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('input-1-state', 'value'),
    State('input-2-state', 'value'),
)
def handle_with_state(n_clicks, value1, value2):
    print("=== handle_with_state === ", n_clicks, value1, value2)
    return '''
        Show value1 {} and value2 {} after clicked {} times.
    '''.format(value1, value2, n_clicks)
