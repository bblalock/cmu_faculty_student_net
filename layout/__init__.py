import dash_bootstrap_components as dbc
from layout.jumbotron import initialize_jumbo_children
from layout.navbar import navbar_children
from layout.cyto import initialize_cyto_children


def get_layout(elements):
    navbar = dbc.NavbarSimple(children=navbar_children,
                              brand="Benjamin Blalock",
                              brand_href="https://github.com/bblalock/cmu_faculty_student_net",
                              color="dark",
                              dark=True,
                              id='nav_bar',
                              fluid=True,
                              )

    jumbotron = dbc.Jumbotron(initialize_jumbo_children(), id='jumbotron')

    card_container = dbc.Card(
        children=initialize_cyto_children(elements),
        inverse=False,
        className='pretty_card',
        id='card_container',
        color='light'
    )

    layout_list = [
        navbar,
        jumbotron,
        card_container,
    ]

    return layout_list
