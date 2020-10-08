import dash_cytoscape as cyto
from utils.cyto import cyto_network

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

cyto.load_extra_layouts()


def initialize_cyto_children(elements):
    children = [
        dbc.CardHeader(html.H3("Advisor-Advisee Social Network Relationships", className="card-title")),
        dbc.CardBody(
            [
                html.P(
                    [],
                ),
                html.Hr(className="my-2"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dbc.CardHeader(html.H4("Controls", className="card-title")),
                                        dbc.CardBody(
                                            [
                                                html.H5("Grouping",
                                                        className="card-title",
                                                        ),
                                                html.Hr(className="my-2"),
                                                dcc.Dropdown(
                                                    id="groupby_dropdown",
                                                    options=[{'label': 'Faculty',
                                                              'value': 'faculty'
                                                              },
                                                             {'label': 'Faculty Type',
                                                              'value': 'faculty_type'
                                                              },
                                                             {'label': 'Student',
                                                              'value': 'student'
                                                              },
                                                             {'label': 'Student Type',
                                                              'value': 'student_type'
                                                              },
                                                             ],
                                                    value=['faculty', 'faculty_type'],
                                                    multi=True,
                                                ),
                                                html.H5("Coloring",
                                                        className="card-title",
                                                        ),
                                                html.Hr(className="my-2"),
                                                dcc.Dropdown(
                                                    id="color_by",
                                                    options=[{'label': 'Community',
                                                              'value': 'community'
                                                              }
                                                             ],
                                                    value='community',
                                                ),
                                                html.H5("Filtering",
                                                        className="card-title",
                                                        ),
                                                html.Hr(className="my-2"),
                                                html.H6("Nodes",
                                                        className="card-title",
                                                        ),
                                                html.Hr(className="my-1"),
                                                daq.BooleanSwitch(
                                                    id='degree_zero_switch',
                                                    on=True,
                                                    label="Display Degree Zero Nodes",
                                                    labelPosition='top',
                                                ),
                                                html.H6("Edges",
                                                        className="card-title",
                                                        ),
                                                html.Hr(className="my-1"),
                                                html.H5("Clicking",
                                                        className="card-title",
                                                        ),
                                                html.Hr(className="my-2"),
                                            ]
                                        ),

                                    ],
                                    className='pretty_container card',
                                )
                            ],
                            className="col-2",
                            style={'display': 'inline-block',
                                   'verticalAlign': 'top',
                                   # 'height': '100%',
                                   'padding': '0'
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
                            className="pretty_card col-10",
                            style={
                                   }
                        )
                    ],
                    className="col-12",
                )
            ]
        )
    ]

    return children
