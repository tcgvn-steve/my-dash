from dash import dcc
from dash import html
from app import app
from dash.dependencies import Input, Output, State
from custom_components import TimelineComponentClass
import dash_bootstrap_components as dbc
items = [{
    "title": "Steve",
    "cardTitle": "Probination",
    "cardSubtitle": "Steve is interested in hitting the gym and playing soccer",
    "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
    "media": {
         "type": "IMAGE",
         "source": {
             "url": "http://someurl/image.jpg"
         }
         }
}, {
    "title": "Ned",
    "cardTitle": "Staff",
    "cardSubtitle": "Ned fancies playing video games",
    "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
    "media": {
        "type": "IMAGE",
        "source": {
             "url": "http://someurl/image.jpg"
        }
    }
}, {
    "title": "Jacob",
    "cardTitle": "Staff",
    "cardSubtitle": "Jacob desires gaming gear",
    "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
    "media": {
        "type": "IMAGE",
        "source": {
             "url": "http://someurl/image.jpg"
        }
    }
}
]
layout = dbc.Container([
    dbc.Row([
        dbc.Col(TimelineComponentClass(
            id='input', items=items, mode='VERTICAL_ALTERNATING'
        ), className="d-inline-block col-md-8"),
        dbc.Col(id='output', className="d-inline-block col-md-4"),
    ])
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)
