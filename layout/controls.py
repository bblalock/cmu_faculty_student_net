import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from functools import reduce

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
                        id='click_control'
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
                    )
                ]
            )
        ]
}

coloring_controls = {
    'header':
        [
            html.H5("Coloring",
                    className="card-title",
                    ),
            html.Hr(className="my-2"),
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.P(['Color Nodes and Edges By:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="color_by",
                        options=[{'label': 'Community',
                                  'value': 'community'
                                  }
                                 ],
                        value='community',
                    )
                ],
            )
        ]
}

filter_controls = {
    'header':
        [
            html.H5("Filtering",
                    className="card-title",
                    ),
            html.Hr(className="my-2"),
        ],
    'body':
        [
            dbc.CardBody(
                [
                    html.H6("Nodes",
                            className="card-title",
                            ),
                    html.Hr(className="my-1"),
                    html.P(['Include Nodes Types:'],
                           className='control-title'
                           ),
                    dcc.Dropdown(
                        id="node_filter_dropdown",
                        options=[{'label': 'Core Faculty',
                                  'value': 'core_faculty'
                                  },
                                 {'label': 'Affiliated Faculty',
                                  'value': 'affiliated_faculty'
                                  },
                                 {'label': 'Related Faculty',
                                  'value': 'related_faculty'
                                  },
                                 {'label': 'Other Faculty',
                                  'value': 'unknown_faculty'
                                  },
                                 {'label': 'Alumni',
                                  'value': 'alumni'
                                  },
                                 {'label': 'Current Students',
                                  'value': 'current_students'
                                  },
                                 ],
                        value=['core_faculty', 'affiliated_faculty',
                               'related_faculty', 'unknown_faculty'
                               ],
                        multi=True,
                    ),
                    html.P(['Include Zero Degree Nodes'],
                           className='control-title'
                           ),
                    daq.BooleanSwitch(
                        id='degree_zero_switch',
                        on=True,
                        style={'align-itmes': 'baseline'}
                    ),
                    html.H6("Edges",
                            className="card-title",
                            ),
                    html.Hr(className="my-1"),
                    html.H6("Set Minimum Edge Weight:",
                            className="card-title",
                            style={'margin-left': '1.0rem'}
                            ),
                    html.P(['Advising Connections:'],
                           className='control-title'
                           ),
                    dcc.Slider(
                        id='edge_weight_slider_adv',
                        min=0,
                        step=1,
                        value=0
                    ),
                    html.P(['Thesis Committee Connections:'],
                           className='control-title'
                           ),
                    dcc.Slider(
                        id='edge_weight_slider_comm',
                        min=0,
                        step=1,
                        value=0
                    ),
                ]
            )
        ]
}

control_components = [
    click_controls,
    grouping_controls,
    coloring_controls,
    filter_controls
]

control_components = reduce(lambda a, b: a + b,
                            [
                                component['header'] + component['body']
                                for i, component in enumerate(control_components)
                            ]
                            )

controls_children = [
    dbc.CardHeader(html.H4("Controls", className="card-title")),
    dbc.CardBody(
        control_components
    ),
]
