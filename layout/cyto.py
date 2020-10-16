import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from utils.cyto import cyto_network

from layout.controls import controls_children
from layout.table import initialize_tables
from constants import NETWORK_HEIGHT

cyto.load_extra_layouts()


def initialize_cyto_children(elements, node_master=None):
    children = [
        dbc.CardHeader([html.H3("Advisor-Advisee Social Network Relationships",
                                className="card-title"
                                )
                        ]
                       ),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.Markdown(
                            """
                    ##### Filter / Explore Graph
                    Clear instructions will go here
                    Use these filters to highlight papers with:
                    * bullet 1
                    * bullet 2
                    
                    Try doing bla bla bla
                    """
                        ),
                        html.Hr(className="my-2"),
                        html.Div(
                            [
                                html.Div(
                                    controls_children,
                                    className='pretty_container card controls',
                                    style={'height': NETWORK_HEIGHT}
                                )
                            ],
                            className="col-3",
                            style={'display': 'inline-block',
                                   'verticalAlign': 'top',
                                   'padding': '0',
                                   'height': '100%'
                                   }
                        ),
                        html.Div(
                            [
                                dcc.Loading(
                                    children=[cyto_network(elements)],
                                    id='cmu_net_loading'
                                ),
                            ],
                            id='cyto_canvas',
                            className="pretty_card col-9",
                        )
                    ],
                    className="col-12",
                )
            ] + initialize_tables()
        )
    ]

    return children
