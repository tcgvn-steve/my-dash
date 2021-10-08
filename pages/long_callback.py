from app import app
import time
import dash
from dash import html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from app import app


layout = html.Div(
    [
        dbc.Alert(id="paragraph_id", children=["Button not clicked"]),
        html.Progress(id="progress_bar"),
        html.P("paragraph_id",
               "Button should be disable while the callback is running"),

        dbc.Button(id="button_id", children="Run Job!"),
        html.P("paragraph_id",
               "Button should be enable while the callback is running"),

        dbc.Button(id="cancel_button_id", children="Cancel Running Job!"),
    ]
)


@ app.long_callback(
    output=Output("paragraph_id", "children"),
    inputs=Input("button_id", "n_clicks"),
    # The second element is the value that the property should be set to while the callback is running,
    # and the third element is the value the property should be set to when the callback completes.
    running=[
        (Output("button_id", "disabled"), True, False),
        (Output("cancel_button_id", "disabled"), False, True),
        (
            Output("progress_bar", "style"),
            {"visibility": "visible"},
            {"visibility": "hidden"},
        ),
    ],
    prevent_initial_call=True,
    cancel=[Input("cancel_button_id", "n_clicks")],
    progress=[Output("progress_bar", "value"), Output("progress_bar", "max")]
)
def callback(set_progress, n_clicks):
    print("=========== n_clicks ", n_clicks)
    if n_clicks:
        time.sleep(2.0)
        total = 10
        for i in range(total):
            time.sleep(0.5)
            set_progress((str(i + 1), str(total)))
        return [f"Clicked {n_clicks} times"]
    return
