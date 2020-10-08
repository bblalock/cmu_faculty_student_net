import dash
import dash_bootstrap_components as dbc

from utils.cyto import format_cyto_edges, format_cyto_nodes
from constants import ROOT_DIR
import pandas as pd

pd.set_option('mode.chained_assignment', None)

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.JOURNAL]
                )
server = app.server

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
                                  font_size_by='join_pagerank',
                                  font_min_size=20,
                                  font_max_size=34,
                                  )

faculty_co_advise_relations = format_cyto_edges(edge_frame[edge_frame.relationship == 'Co-Advised'],
                                                classes='co_advised_edge',
                                                size_by='weight',
                                                min_size=5,
                                                max_size=8,
                                                opacity_by='weight',
                                                min_opacity=0.4,
                                                max_opacity=0.7,
                                                font_size_by='weight',
                                                font_min_size=18,
                                                font_max_size=22,
                                                )

faculty_co_committee_relations = format_cyto_edges(edge_frame[edge_frame.relationship == 'Co-Committee'],
                                                   classes='co_committee_edge',
                                                   size_by='weight',
                                                   min_size=3,
                                                   max_size=6,
                                                   opacity_by='weight',
                                                   min_opacity=0.3,
                                                   max_opacity=0.6,
                                                   font_size_by='weight',
                                                   font_min_size=12,
                                                   font_max_size=16,
                                                   )

cyto_elements = [*faculty_root_nodes,
                 *faculty_type_nodes,
                 *faculty_nodes,
                 *faculty_co_advise_relations,
                 *faculty_co_committee_relations
                 ]
