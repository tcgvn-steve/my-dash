import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import json
from dash.exceptions import PreventUpdate

layout = html.Div([
    html.H3("This is tutorial about advanced callback"),
    html.H4("Example 1: It will prevent update when you don't type."),
    html.P('Enter a composite number to see its prime factors'),
    dcc.Input(id='num', type='number', debounce=True, min=1, step=1),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out'),
    html.Br(),
    html.H4("Example 2: dash.callback_context."),
    html.Button('Button 1', id='btn-1'),
    html.Button('Button 2', id='btn-2'),
    html.Button('Button 3', id='btn-3'),
    html.Div(id='container'),
    dcc.Store(id='intermediate-value'),
])


@app.callback(Output('intermediate-value', 'data'),
              Input('btn-1', 'n_clicks'),
              Input('btn-2', 'n_clicks'),
              Input('btn-3', 'n_clicks'))
def store_data(click_1, click_2, click_3):
    if click_1 or click_2 or click_1:
        data = {
            'btn-1': click_1,
            'btn-2': click_2,
            'btn-3': click_3
        }
        # ctx = dash.callback_context
        # print(" store_data ctx.triggered: ", ctx.triggered)
        # if ctx.triggered and ctx.triggered[0].get('prop_id', None):
        #     count_click = ctx.triggered[0].get('value')
        #     btn_id = ctx.triggered[0].get('prop_id').split('.')[0]
        #     data[btn_id] = count_click
        print(" store_data data: ", data)

        return data
    raise PreventUpdate


@app.callback(Output('container', 'children'),
              Input('intermediate-value', 'data'))
def show_data(data):
    ctx = dash.callback_context
    data = {} if not data else data
    print(" check_status_element data: ", data)

    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Table([
            html.Tr([
                html.Td(k), html.Td(v)
            ]) for k, v in data.items()
        ]),
        html.Pre(ctx_msg)
    ])


@app.callback(
    Output('out', 'children'),
    Output('err', 'children'),
    Input('num', 'value')
)
def show_factors(num):
    if num is None:
        # PreventUpdate prevents ALL outputs updating
        print("=== PreventUpdate ")
        raise dash.exceptions.PreventUpdate

    factors = prime_factors(num)
    if len(factors) == 1:
        # dash.no_update prevents any single output updating
        # (note: it's OK to use for a single-output callback too)
        return dash.no_update, '{} is prime!'.format(num)

    return '{} is {}'.format(num, ' * '.join(str(n) for n in factors)), ''


def prime_factors(num):
    n, i, out = num, 2, []
    while i * i <= n:
        if n % i == 0:
            n = int(n / i)
            out.append(i)
        else:
            i += 1 if i == 2 else 2
    out.append(n)
    return out
