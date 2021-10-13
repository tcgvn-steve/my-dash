from dash import dcc
from dash import html
from app import app
from dash.dependencies import Input, Output, State
from custom_components import TimelineComponentClass
import dash_bootstrap_components as dbc
items = [{
    "title": "2021",
    "cardTitle": "Steve",
    "cardSubtitle": "Steve is interested in hitting the gym and playing soccer",
    "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
    "media": {
         "type": "IMAGE",
         "source": {
             "url": "/assets/avatar.jpg"
         }
         }
}, {
    "title": "2020",
    "cardTitle": "Ned",
    "cardSubtitle": "Ned fancies playing video games",
    "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
    "media": {
        "type": "IMAGE",
        "source": {
             "url": "/assets/avatar2.png"
        }
    }
}, {
    "title": "2019",
    "cardTitle": "Jacob",
    "cardSubtitle": "Jacob desires gaming gear",
    "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
    "media": {
        "type": "IMAGE",
        "source": {
             "url": "/assets/avatar.jpg"
        }
    }
}
]

layout = dbc.Container([
    dbc.Row([
        dbc.Col(TimelineComponentClass(
            id='input', items=items, mode='VERTICAL_ALTERNATING'
        ), className="d-inline-block col-md-8"),
        dbc.Col(id='output', children="", className="d-inline-block col-md-4"),
    ])
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    res = items[0]
    if value:
        print("=== value ", type(value))
        print("=== value ", (value))
        import json
        res = json.loads(value)
        print("=== res ", (res))
        print("=== res ", (res['cardTitle']))

    return html.Div([
        html.H2(children=("{}: {}".format(
            res['title'], res['cardTitle']))),
        dbc.Col(children="{}. {}".format(
            res['cardSubtitle'], res['cardDetailedText']))
    ])
