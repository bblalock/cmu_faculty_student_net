import dash
import dash_bootstrap_components as dbc
from flask import send_file
from utils.cyto import format_cyto_edges, format_cyto_nodes, add_node_formatting
from constants import ROOT_DIR
import pandas as pd

pd.set_option('mode.chained_assignment', None)

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.JOURNAL]
                )


@app.server.route('/resumeDownload')
def download_csv():
    return send_file(ROOT_DIR + '/data/pdf/bblalock_resume.pdf',
                     attachment_filename='bblalock_resume.pdf',
                     as_attachment=True
                     )


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

node_frame = add_node_formatting(node_frame,
                                 label='id',
                                 size_by='joint_pagerank',
                                 min_size=40,
                                 max_size=120,
                                 opacity_by='joint_pagerank',
                                 min_opacity=0.3,
                                 max_opacity=0.8,
                                 font_size_by='joint_pagerank',
                                 font_min_size=20,
                                 font_max_size=34,
                                 )

core_faculty_nodes = format_cyto_nodes(node_frame[node_frame['faculty_type'] == 'core'],
                                       parent='faculty_type',
                                       classes='faculty_node core_faculty',
                                       )

affiliated_faculty_nodes = format_cyto_nodes(node_frame[node_frame['faculty_type'] == 'affiliated'],
                                             parent='faculty_type',
                                             classes='faculty_node affiliated_faculty',
                                             )

related_faculty_nodes = format_cyto_nodes(node_frame[node_frame['faculty_type'] == 'related'],
                                          parent='faculty_type',
                                          classes='faculty_node related_faculty',
                                          )

unknown_faculty_nodes = format_cyto_nodes(node_frame[node_frame['faculty_type'] == 'unknown'],
                                          parent='faculty_type',
                                          classes='faculty_node unknown_faculty',
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

cyto_elements = {
    'faculty_root': faculty_root_nodes,
    'faculty_type': faculty_type_nodes,
    'core_faculty': core_faculty_nodes,
    'affiliated_faculty': affiliated_faculty_nodes,
    'related_faculty': related_faculty_nodes,
    'unknown_faculty': unknown_faculty_nodes,
    'co_advised_edge': faculty_co_advise_relations,
    'co_committee_edge': faculty_co_committee_relations
}
