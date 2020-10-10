import dash
import dash_bootstrap_components as dbc
from flask import send_file
from utils.cyto import format_cyto_edges, format_cyto_nodes, add_node_formatting
from constants import ROOT_DIR
import pandas as pd

pd.set_option('mode.chained_assignment', None)

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.CYBORG]
                )


# app.config['suppress_callback_exceptions'] = True


@app.server.route('/resumeDownload')
def download_csv():
    return send_file(ROOT_DIR + '/data/pdf/bblalock_resume.pdf',
                     attachment_filename='bblalock_resume.pdf',
                     as_attachment=True
                     )


faculty_node_frame = pd.read_csv(ROOT_DIR + '/data/app/faculty_node_frame.csv')
faculty_edge_frame = pd.read_csv(ROOT_DIR + '/data/app/faculty_edge_frame.csv')

faculty_root_nodes = format_cyto_nodes(faculty_node_frame[['entity_type']].drop_duplicates(),
                                       classes='entity_root_node',
                                       label='entity_type'
                                       )

faculty_type_nodes = format_cyto_nodes(faculty_node_frame[['entity_type', 'entity_subtype']].drop_duplicates(),
                                       parent='entity_type',
                                       classes='entity_type_node',
                                       label='entity_subtype'
                                       )

faculty_node_frame = add_node_formatting(faculty_node_frame,
                                         label='id',
                                         size_by='pagerank',
                                         min_size=40,
                                         max_size=120,
                                         opacity_by='pagerank',
                                         min_opacity=0.3,
                                         max_opacity=0.8,
                                         font_size_by='pagerank',
                                         font_min_size=20,
                                         font_max_size=34,
                                         )

core_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'core'],
                                       parent='entity_subtype',
                                       classes='entity_node core_faculty',
                                       )

affiliated_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'affiliated'],
                                             parent='entity_subtype',
                                             classes='entity_node affiliated_faculty',
                                             )

related_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'related'],
                                          parent='entity_subtype',
                                          classes='entity_node related_faculty',
                                          )

unknown_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'unknown'],
                                          parent='entity_subtype',
                                          classes='entity_node unknown_faculty',
                                          )

faculty_co_advise_relations = format_cyto_edges(faculty_edge_frame[faculty_edge_frame.relationship == 'Co-Advised'],
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

faculty_co_committee_relations = format_cyto_edges(
    faculty_edge_frame[faculty_edge_frame.relationship == 'Co-Committee'],
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

student_node_frame = pd.read_csv(ROOT_DIR + '/data/app/student_node_frame.csv')
student_edge_frame = pd.read_csv(ROOT_DIR + '/data/app/student_edge_frame.csv')

student_root_nodes = format_cyto_nodes(student_node_frame[['entity_type']].drop_duplicates(),
                                       classes='entity_root_node',
                                       label='entity_type'
                                       )

# student_type_nodes = format_cyto_nodes(student_node_frame[['entity_type', 'entity_subtype']].drop_duplicates(),
#                                        parent='entity_type',
#                                        classes='entity_type_node',
#                                        label='entity_subtype'
#                                        )

student_node_frame = add_node_formatting(student_node_frame,
                                         label='id',
                                         size_by='pagerank',
                                         min_size=40,
                                         max_size=120,
                                         opacity_by='pagerank',
                                         min_opacity=0.3,
                                         max_opacity=0.8,
                                         font_size_by='pagerank',
                                         font_min_size=20,
                                         font_max_size=34,
                                         )

current_student_nodes = format_cyto_nodes(student_node_frame[student_node_frame['entity_subtype'] == 'current_student'],
                                          parent='entity_type',
                                          classes='entity_node current_student',
                                          )

alumni_student_nodes = format_cyto_nodes(student_node_frame[student_node_frame['entity_subtype'] == 'alumni'],
                                         parent='entity_type',
                                         classes='entity_node alumni_student',
                                         )

student_co_advise_relations = format_cyto_edges(student_edge_frame[student_edge_frame.relationship == 'Co-Advised'],
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

student_co_committee_relations = format_cyto_edges(
    student_edge_frame[student_edge_frame.relationship == 'Co-Committee'],
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
    # faculty
    'entity_root_node': faculty_root_nodes,
    'entity_type_node': faculty_type_nodes,
    'core_faculty': core_faculty_nodes,
    'affiliated_faculty': affiliated_faculty_nodes,
    'related_faculty': related_faculty_nodes,
    'unknown_faculty': unknown_faculty_nodes,
    'faculty_co_advised_edge': faculty_co_advise_relations,
    'faculty_co_committee_edge': faculty_co_committee_relations,
    # Students
    # 'student_root_node': student_root_nodes,
    # # 'student_type_node': student_type_nodes,
    # 'current_students': current_student_nodes,
    # 'alumni_students': alumni_student_nodes,
    # 'student_co_advised_edge': student_co_advise_relations,
    # 'student_co_committee_edge': student_co_committee_relations,

}
