import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
from app import app
import json

layout = html.Div([
    html.Button("Add Filter", id="add-filter", n_clicks=0),
    html.Div(id='dropdown-container', children=[]),
    html.Div(id='dropdown-container-output'),
    html.Div(id='ctx-output')
])


@app.callback(
    Output('dropdown-container', 'children'),
    Input('add-filter', 'n_clicks'),
    State('dropdown-container', 'children'))
def display_dropdowns(n_clicks, children):
    print("==== n_clicks ", n_clicks)
    print("==== children ", children)

    new_dropdown = dcc.Dropdown(
        id={

            'index': n_clicks
        },
        options=[{'label': i, 'value': i}
                 for i in ['NYC', 'MTL', 'LA', 'TOKYO']]
    )
    children.append(new_dropdown)
    print("==== children ", children)
    return children


@app.callback(
    Output('dropdown-container-output', 'children'),
    Input({'index': ALL}, 'value')
)
def display_output(values):
    print("==== values ", values)

    if len(values) == 0 or (len(values) >= 1 and values[0] == None):
        # raise dash.exceptions.PreventUpdate
        return
    return html.Div([
        html.Div('Dropdown {} = {}'.format(i + 1, value))
        for (i, value) in enumerate(values)
    ])


@app.callback(
    Output('ctx-output', 'children'),
    Input('add-filter', 'n_clicks')
)
def display_ctx(n_clicks):
    if n_clicks:
        ctx = dash.callback_context
        ctx_msg = json.dumps({
            'states': ctx.states,
            'triggered': ctx.triggered,
            'inputs': ctx.inputs,
            'outputs_list': ctx.outputs_list
        }, indent=2)

        return html.Pre(ctx_msg)


if __name__ == '__main__':
    app.run_server(debug=True)
