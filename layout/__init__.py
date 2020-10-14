import dash_bootstrap_components as dbc
from layout.jumbotron import initialize_jumbo_children
from layout.navbar import navbar_children
from layout.cyto import initialize_cyto_children
from layout.table import initialize_tables

def get_layout(elements, node_master):
    navbar = dbc.NavbarSimple(children=navbar_children,
                              brand="Benjamin Blalock",
                              brand_href="https://github.com/bblalock/cmu_faculty_student_net",
                              color="dark",
                              dark=True,
                              id='nav_bar',
                              fluid=True,
                              )

    jumbotron = dbc.Jumbotron(initialize_jumbo_children(), id='jumbotron')

    cyto_container = dbc.Card(
        children=initialize_cyto_children(elements, node_master),
        inverse=False,
        className='pretty_card',
        id='cyto_container',
        # color='dark'
    )

    layout_list = [
        navbar,
        jumbotron,
        cyto_container
    ]

    return layout_list
