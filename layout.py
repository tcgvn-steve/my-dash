import dash
import dash_html_components as html
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
            dac.SidebarHeader(children="Members"),
            dcc.Link(children=dac.SidebarMenuItem(
                id='tab_cards', label='Users', icon='box'), href='/users'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_social_cards',
                                                  label='Groups', icon='id-card'), href='/groups'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_tab_cards',
                                                  label='Permission', icon='image'), href='/permissions'),
            dac.SidebarHeader(children="Products"),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_basic_boxes',
                                                  label='products', icon='desktop'), href='/products'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_value_boxes',
                                                  label='Categories', icon='suitcase'), href='/categories'),
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
