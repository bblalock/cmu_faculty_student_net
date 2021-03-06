import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from functools import reduce
from app_setup import communities, community_df
from utils.plots import community_bar

click_controls = {
    'header':
        [
            html.H5("Clicking",
                    className="card-title",
                    ),
            html.Hr(className="my-2")
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.P(['Click Nodes To:'],
                           className='control-title'
                           ),
                    html.Hr(className="my-1"),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Highlight Connections', 'value': 'highlight'},
                            {'label': 'Expand Faculty Connections', 'value': 'expand_fac'},
                            {'label': 'Expand Student Connections', 'value': 'expand_stu'},
                        ],
                        value='highlight',
                        id='click_control', className="dash-bootstrap"
                    )
                ]
            )
        ]
}

grouping_controls = {
    'header':
        [
            html.H5("Grouping",
                    className="card-title",
                    ),
            html.Hr(className="my-2")
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.P(['Group Nodes By:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="groupby_dropdown",
                        options=[
                            {'label': 'Faculty Type',
                             'value': 'entity_type_node'
                             },
                            {'label': 'Student',
                             'value': 'student_root_node'
                             },
                            {'label': 'Student Type',
                             'value': 'student_type_node'
                             },
                        ],
                        value=['entity_type_node'],
                        multi=True, className="dash-bootstrap"
                    )
                ]
            )
        ]
}

community_controls = {
    'header':
        [
            html.H5("Communities",
                    className="card-title",
                    ),
            html.Hr(className="my-2"),
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.P(['Communities by Size:'],
                           className='control-title'
                           ),
                    html.Div(children=[
                        dcc.Graph(
                            id="community_bar",
                            figure=community_bar(community_df),
                            config={"displayModeBar": False},
                        )
                    ],
                        id='community_bar_container'
                    ),
                    html.P(['Include Communities:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="community_dropdown",
                        options=[{'label': 'All Communities',
                                  'value': 'all'
                                  },
                                 ] + [{'label': 'Community ' + str(comm_label),
                                       'value': comm_label
                                       }
                                      for comm_label in sorted(communities)
                                      ]
                        ,
                        value=['all'],
                        multi=True,
                        className="dash-bootstrap"
                    )
                ],
                style={'padding-right': 0,
                       'padding-left': 5
                       }
            )
        ]
}

node_controls = {
    'header':
        [
            html.H5("Nodes",
                    className="card-title",
                    ),
            html.Hr(className="my-2"),
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.P(['Include Zero Degree Nodes'],
                           className='control-title'
                           ),
                    daq.BooleanSwitch(
                        id='degree_zero_switch',
                        on=True,
                        style={'align-items': 'baseline'}, className="dash-bootstrap"
                    ),
                    html.P(['Size Nodes by:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="node_size_dropdown",
                        options=[{'label': 'MultiGraph PageRank ',
                                  'value': 'pagerank'
                                  },
                                 ],
                        value='pagerank',
                        multi=False,
                        className="dash-bootstrap",
                    ),
                    html.P(['Include Nodes Types:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="node_filter_dropdown",
                        options=[{'label': 'Core Faculty',
                                  'value': 'entity_node faculty core'
                                  },
                                 {'label': 'Affiliated Faculty',
                                  'value': 'entity_node faculty affiliated'
                                  },
                                 {'label': 'Related Faculty',
                                  'value': 'entity_node faculty related'
                                  },
                                 {'label': 'Other Faculty',
                                  'value': 'entity_node faculty unknown'
                                  },
                                 {'label': 'Alumni',
                                  'value': 'entity_node student alumni'
                                  },
                                 {'label': 'Current Students',
                                  'value': 'entity_node student current'
                                  },
                                 ],
                        value=['entity_node faculty core', 'entity_node faculty affiliated',
                               'entity_node faculty related', 'entity_node faculty unknown',
                               'entity_node student alumni', 'entity_node student current'
                               ],
                        multi=True,
                        className="dash-bootstrap"
                    )
                ],
                style={'padding-right': 0,
                       'padding-left': 5
                       }
            )
        ]
}

edge_controls = {
    'header':
        [
            html.H5("Edges",
                    className="card-title",
                    ),
            html.Hr(className="my-2"),
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.P(['Include Edge Types:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="edge_filter_dropdown",
                        options=[{'label': 'Co-Advised Student',
                                  'value': 'co_advised_edge faculty'
                                  },
                                 {'label': 'Co-Advised By Faculty',
                                  'value': 'co_advised_edge student'
                                  },
                                 {'label': 'Co-Served on Committee',
                                  'value': 'co_committee_edge faculty'
                                  },
                                 {'label': 'Advisor-Advisee',
                                  'value': 'bipartite_advised_edge'
                                  }
                                 ],
                        value=['co_advised_edge faculty', 'co_advised_edge student',
                               'co_committee_edge faculty', 'bipartite_advised_edge'
                               ],
                        multi=True,
                        className="dash-bootstrap",
                    ),
                    html.H6("Set Minimum Edge Weight:",
                            className="card-title",
                            # style={'margin-top': '1.0rem'}
                            ),
                    html.P(['Advising Connections:'],
                           className='control-title'
                           ),
                    dcc.Slider(
                        id='edge_weight_slider_adv',
                        min=1,
                        step=1,
                        value=1,
                        className="dash-bootstrap"
                    ),
                    html.P(['Committee Connections:'],
                           className='control-title'
                           ),
                    dcc.Slider(
                        id='edge_weight_slider_comm',
                        min=1,
                        step=1,
                        value=3,
                        className="dash-bootstrap"
                    ),
                ],
                style={'padding-right': 0,
                       'padding-left': 5
                       }
            )
        ]
}

control_components = [
    # click_controls,
    # grouping_controls,
    community_controls,
    node_controls,
    edge_controls
]

control_components = reduce(lambda a, b: a + b,
                            [
                                component['header'] + component['body']
                                for i, component in enumerate(control_components)
                            ]
                            )

controls_children = [
    dbc.CardHeader([html.Div([html.H4("Controls", className="card-title", style={'display': 'inline-block'}),
                              dbc.Button('Redraw Graph',
                                         id='redraw_button',
                                         n_clicks=0,
                                         outline=True,
                                         color='dark',
                                         size='sm'
                                         )
                              ],
                             style={'width': '100%',
                                    'display': 'flex',
                                    'position': 'relative',
                                    'align-items': 'center',
                                    'justify-content': 'space-between'
                                    }
                             )
                    ]
                   ),
    dbc.CardBody(
        children=control_components
    ),
]
