import dash
from dash import html
import dash_admin_components as dac
from dash.dependencies import Input, Output
from dash import dcc

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar
right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="",
    header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
                children="message 1",
                date="today"
        ),
        dac.NavbarDropdownItem(
            children="message 2",
            date="yesterday"
        ),
    ]
)

navbar = dac.Navbar(color="white",
                    text="",
                    children=right_ui)

# Sidebar
sidebar = dac.Sidebar(
    dac.SidebarMenu(
        [
            dac.SidebarHeader(children="Basic"),
            dcc.Link(children=dac.SidebarMenuItem(
                id='tab_cards', label='Graph', icon='box', className='nav-padding'), href='/graph'),

            # dac.SidebarMenuItem(
            #     id='tab_cards1', label='Graph', icon='box'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_social_cards',
                                                  label='Chained Callback', icon='id-card'), href='/chained_callback'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_tab_cards',
                                                  label='State', icon='image'), href='/state'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_basic_boxes',
                                                  label='dccDtore', icon='desktop'), href='/dcc_store'),
            dac.SidebarHeader(children="Callback"),

            dcc.Link(children=dac.SidebarMenuItem(id='advanced_callback',
                                                  label='Advanced Callback', icon='suitcase'), href='/advanced_callback'),
            dcc.Link(children=dac.SidebarMenuItem(id='client_callback',
                                                  label='Client Callback', icon='suitcase'), href='/client_callback'),
            dcc.Link(children=dac.SidebarMenuItem(id='pattern_callback_all',
                                                  label='Pattern callback all', icon='suitcase'), href='/pattern_callback_all'),
            dcc.Link(children=dac.SidebarMenuItem(id='pattern_callback_matchpattern_callback_match',
                                                  label='Pattern callback match', icon='suitcase'), href='/pattern_callback_match'),
            dcc.Link(children=dac.SidebarMenuItem(id='long_callback',
                                                  label='Long Callback', icon='suitcase'), href='/long_callback'),
            dac.SidebarHeader(children="Custom Component"),
            dcc.Link(children=dac.SidebarMenuItem(id='timeline_component',
                                                  label='Timeline Compopnent', icon='suitcase'), href='/timeline_component'),

        ]
    ),
    title='Dash Admin',
    skin="light",
    color="primary",
    brand_color="primary",
    url="",
    src="https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    elevation=3,
    opacity=0.8
)


# Body
body = dac.Body([
    dcc.Location(id='url'),
    html.Div(id='content', children="")
])

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Put different components here!"),
    ],
    title="My right sidebar",
    skin="light"
)

# Footer
footer = dac.Footer(
    html.A("@Steve, TCG",
           href="",
           target="_blank",
           ),
    right_text="2021"
)
