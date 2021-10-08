import dash
from dash import html
import dash_admin_components as dac
from dash.dependencies import Input, Output
from layout import navbar, sidebar, body, controlbar, footer
from app import app
from pages import (graph, chained_callback, state, dcc_store, categories,
                   advanced_callback, client_callback, pattern_callback_match, pattern_callback_all,
                   long_callback)

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
server = app.server
# =============================================================================
# Navigate App
# =============================================================================


@app.callback(
    Output('content', 'children'),
    Input('url', 'pathname')
)
def display(pathname):
    if pathname == '/':
        return html.Div([
            html.Br(),
            html.H4(children='Here you are Home Page'),
        ])
    if pathname == '/graph':
        return graph.layout
    if pathname == '/chained_callback':
        return chained_callback.layout
    if pathname == '/state':
        return state.layout
    if pathname == '/dcc_store':
        return dcc_store.layout
    if pathname == '/categories':
        return categories.layout
    if pathname == '/advanced_callback':
        return advanced_callback.layout
    if pathname == '/client_callback':
        return client_callback.layout
    if pathname == '/pattern_callback_match':
        return pattern_callback_match.layout
    if pathname == '/pattern_callback_all':
        return pattern_callback_all.layout
    if pathname == '/long_callback':
        return long_callback.layout
    return '404'


# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=True)
