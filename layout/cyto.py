import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from utils.cyto import cyto_network

from layout.controls import controls_children
from layout.legend import legend_children
from layout.table import initialize_tables
from constants import NETWORK_HEIGHT

cyto.load_extra_layouts()


def initialize_cyto_children(elements):
    children = [
        dbc.CardHeader([html.H3("Advisor-Advisee Social Network Relationships",
                                className="card-title"
                                )
                        ]
                       ),
        dbc.CardBody(
            [
                dbc.Col(
                    legend_children
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(controls_children,
                                     style={'height': '100%'}
                                     ),
                            md=3,
                            style={'overflow': 'auto',
                                   # 'height': NETWORK_HEIGHT
                                   },
                        ),
                        dbc.Col(
                            dbc.Card(
                                dcc.Loading(
                                    children=[cyto_network(elements)],
                                    id='cmu_net_loading'
                                ),
                                style={'height': '100%'}
                            ),
                            md=9,
                        )
                    ]
                )
            ] +
            initialize_tables()
        )
    ]
    return children
