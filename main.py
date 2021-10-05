import dash
import dash_html_components as html
import dash_admin_components as dac
from dash.dependencies import Input, Output
from layout import navbar, sidebar, body, controlbar, footer
from app import app
from pages import users, groups, permissions, products, categories

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])


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
    if pathname == '/users':
        return users.layout
    if pathname == '/groups':
        return groups.layout
    if pathname == '/permissions':
        return permissions.layout
    if pathname == '/products':
        return products.layout
    if pathname == '/categories':
        return categories.layout
    return '404'


# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=True)
