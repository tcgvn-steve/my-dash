
from dash import html
from dash import dcc

from dash.dependencies import Input, Output
from app import app
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate


layout = html.Div([
    dbc.Input(id="input", placeholder="Type something...", type="number"),
    dbc.Label("You can see in console code at runtime"),
    html.Table([
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
    ]),
])


app.clientside_callback(
    """
    function(x) {
        if (x === undefined){
            return 0
        };
        console.log("function clientside_callback: ",x*x);
        return x*x
    }
    """,
    Output('x^x', 'children'),
    Input('input', 'value')
)
