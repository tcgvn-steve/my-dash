from dash import dcc
import dash_html_components as html

layout = html.Div([
    html.H3('Categories Managers'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
])
