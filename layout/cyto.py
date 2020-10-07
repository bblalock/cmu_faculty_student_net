import pandas as pd
import dash_cytoscape as cyto
from constants import COSE_BILKENT_LAYOUT_OPTIONS, NETWORK_HEIGHT, DEFAULT_STYLESHEET, ROOT_DIR
from utils.cyto import format_cyto_edges, format_cyto_nodes

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

cyto.load_extra_layouts()


def initialize_cyto_children():
    node_frame = pd.read_csv(ROOT_DIR + '/data/app/joint_node_frame.csv')
    edge_frame = pd.read_csv(ROOT_DIR + '/data/app/joint_edge_frame.csv')

    faculty_root_nodes = format_cyto_nodes(node_frame[['entity_type']].drop_duplicates(),
                                           classes='faculty_root_node',
                                           label='entity_type'
                                           )

    faculty_type_nodes = format_cyto_nodes(node_frame[['entity_type', 'faculty_type']].drop_duplicates(),
                                           parent='entity_type',
                                           classes='faculty_type_node',
                                           label='faculty_type'
                                           )

    faculty_nodes = format_cyto_nodes(node_frame,
                                      parent='faculty_type',
                                      classes='faculty_node',
                                      size_by='joint_pagerank',
                                      min_size=40,
                                      max_size=120,
                                      opacity_by='joint_pagerank',
                                      min_opacity=0.3,
                                      max_opacity=0.8,
                                      )

    faculty_co_advise_relations = format_cyto_edges(edge_frame[edge_frame.relationship == 'Co-Advised'],
                                                    classes='co_advised_edge',
                                                    size_by='weight',
                                                    min_size=5,
                                                    max_size=8,
                                                    opacity_by='weight',
                                                    min_opacity=0.4,
                                                    max_opacity=0.7,
                                                    )

    faculty_co_committee_relations = format_cyto_edges(edge_frame[edge_frame.relationship == 'Co-Committee'],
                                                       classes='co_committee_edge',
                                                       size_by='weight',
                                                       min_size=3,
                                                       max_size=6,
                                                       opacity_by='weight',
                                                       min_opacity=0.3,
                                                       max_opacity=0.7,
                                                       )

    children = [
        dbc.CardHeader(html.H5("Network Title", className="card-title")),
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
                                        html.H6("Plot Type:",
                                                className="card-title",
                                                ),
                                        dcc.RadioItems(
                                            id='ti_plot_type_radio',
                                            options=[
                                                {'label': 'SunBurst', 'value': 'sunburst'},
                                                {'label': 'TreeMap', 'value': 'treemap'}
                                            ],
                                            value='treemap',
                                            labelStyle={'display': 'inline-block', 'padding': '0rem 1rem'}
                                        ),
                                        html.H6("Split Patients by:",
                                                className="card-title",
                                                ),
                                        html.Hr(className="my-2"),
                                        dcc.Dropdown(
                                            id="ti_prefix_filter",
                                            options=[{'label': 'test', 'value': 'test'}],
                                            value='test',
                                            multi=True,
                                        ),
                                        html.H6("Display Lines of Therapy:",
                                                className="card-title",
                                                ),
                                        daq.BooleanSwitch(
                                            id='progression_switch',
                                            on=False,
                                            label="Only show Patients having Progressed to the Final Line",
                                            labelPosition="top",
                                            disabled=True
                                        ),
                                        html.Hr(className="my-2"),
                                        dcc.Dropdown(
                                            id="ti_line_filter",
                                            options=[{'label': 'test', 'value': 'test'}],
                                            value='test',
                                            multi=True,
                                            disabled=True
                                        ),
                                        html.H6("Color by:",
                                                className="card-title",
                                                ),
                                        html.Hr(className="my-2"),
                                        dcc.Dropdown(
                                            id="color_by",
                                            options=[{'label': 'Community',
                                                      'value': 'Community'
                                                      }
                                                     ],
                                            value='test',
                                        )

                                    ],
                                    className='pretty_container',
                                )
                            ],
                            className="col-3",
                            style={'display': 'inline-block',
                                   'verticalAlign': 'top',
                                   'height': '100%',
                                   'padding': '0'
                                   }
                        ),
                        html.Div(
                            [
                                dcc.Loading(
                                    cyto.Cytoscape(
                                        id='cmu_net',
                                        layout=COSE_BILKENT_LAYOUT_OPTIONS,
                                        style={'width': '100%', 'height': NETWORK_HEIGHT},
                                        stylesheet=DEFAULT_STYLESHEET,
                                        elements=[
                                            *faculty_root_nodes,
                                            *faculty_type_nodes,
                                            *faculty_nodes,
                                            *faculty_co_advise_relations,
                                            *faculty_co_committee_relations
                                        ]
                                    ),
                                ),
                            ],
                            className="col-9",
                            style={'display': 'inline-block',
                                   'verticalAlign': 'top',
                                   'height': '100%',
                                   'padding': '0'
                                   }
                        )
                    ],
                    className="col-12",
                )
            ]
        )
    ]

    return children
