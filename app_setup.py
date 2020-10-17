import dash
from flask import send_file
from utils.cyto import format_cyto_edges, format_cyto_nodes, add_node_formatting
from utils.data_table import create_faculty_student_table_dfs, create_community_color_dict
from constants import ROOT_DIR, FILTERABLE_EDGE_CLASSES
from functools import reduce
import pandas as pd

pd.set_option('mode.chained_assignment', None)

app = dash.Dash(__name__)


@app.server.route('/resumeDownload')
def download_csv():
    return send_file(ROOT_DIR + '/data/pdf/bblalock_resume.pdf',
                     attachment_filename='bblalock_resume.pdf',
                     as_attachment=True
                     )


node_master = pd.read_csv(ROOT_DIR + '/data/app/master_node_frame.csv')
# node_master = node_master[node_master['degree']>0]
edge_master = pd.read_csv(ROOT_DIR + '/data/app/master_edge_frame.csv')

faculty_df, student_df = create_faculty_student_table_dfs(node_master=node_master)
community_color_dict = create_community_color_dict(node_master=node_master)

community_df = node_master \
    .groupby(['community', 'community_color'], as_index=False)['id'] \
    .count() \
    .rename(columns={'id': 'count'}) \
    .sort_values(['count'], ascending=False) \
    .reset_index(drop=True)
communities = community_df.community.tolist()

faculty_node_frame = node_master[node_master['entity_type'] == 'faculty']
faculty_edge_frame = pd.read_csv(ROOT_DIR + '/data/app/faculty_edge_frame.csv')
faculty_edge_frame = pd.merge(faculty_edge_frame[['source', 'target', 'relationship']],
                              edge_master,
                              on=['source', 'target', 'relationship'],
                              how='inner'
                              )

faculty_root_nodes = format_cyto_nodes(faculty_node_frame[['entity_type']].drop_duplicates(),
                                       classes='entity_root_node faculty',
                                       label='entity_type'
                                       )

faculty_type_nodes = format_cyto_nodes(faculty_node_frame[['entity_type', 'entity_subtype']].drop_duplicates(),
                                       parent='entity_type',
                                       classes='entity_type_node faculty',
                                       label='entity_subtype'
                                       )

faculty_node_frame = add_node_formatting(faculty_node_frame,
                                         label='id',
                                         size_by='pagerank',
                                         min_size=20,
                                         max_size=160,
                                         opacity_by='pagerank',
                                         min_opacity=0.6,
                                         max_opacity=0.9,
                                         font_size_by='pagerank',
                                         font_min_size=20,
                                         font_max_size=34,
                                         )

core_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'core'],
                                       parent='entity_subtype',
                                       classes='entity_node faculty core',
                                       )

affiliated_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'affiliated'],
                                             parent='entity_subtype',
                                             classes='entity_node faculty affiliated',
                                             )

related_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'related'],
                                          parent='entity_subtype',
                                          classes='entity_node faculty related',
                                          )

unknown_faculty_nodes = format_cyto_nodes(faculty_node_frame[faculty_node_frame['entity_subtype'] == 'unknown'],
                                          parent='entity_subtype',
                                          classes='entity_node faculty unknown',
                                          )

faculty_co_advise_relations = format_cyto_edges(faculty_edge_frame[faculty_edge_frame.relationship == 'Co-Advised'],
                                                classes='co_advised_edge faculty',
                                                size_by='weight',
                                                min_size=12,
                                                max_size=18,
                                                opacity_by='weight',
                                                min_opacity=0.4,
                                                max_opacity=0.9,
                                                font_size_by='weight',
                                                font_min_size=18,
                                                font_max_size=22,
                                                )

faculty_co_committee_relations = format_cyto_edges(
    faculty_edge_frame[faculty_edge_frame.relationship == 'Co-Committee'],
    classes='co_committee_edge faculty',
    size_by='weight',
    min_size=8,
    max_size=14,
    opacity_by='weight',
    min_opacity=0.3,
    max_opacity=0.8,
    font_size_by='weight',
    font_min_size=12,
    font_max_size=16,
)

student_node_frame = node_master[node_master['entity_type'] == 'student']
student_edge_frame = pd.read_csv(ROOT_DIR + '/data/app/student_edge_frame.csv')
student_edge_frame = student_edge_frame[['source', 'target', 'relationship']]
student_edge_frame = pd.merge(student_edge_frame,
                              edge_master,
                              on=['source', 'target', 'relationship'],
                              how='inner'
                              )

student_root_nodes = format_cyto_nodes(student_node_frame[['entity_type']].drop_duplicates(),
                                       classes='entity_root_node student',
                                       label='entity_type'
                                       )

# student_type_nodes = format_cyto_nodes(student_node_frame[['entity_type', 'entity_subtype']].drop_duplicates(),
#                                        parent='entity_type',
#                                        classes='entity_type_node student',
#                                        label='entity_subtype'
#                                        )

student_node_frame = add_node_formatting(student_node_frame,
                                         label='id',
                                         size_by='pagerank',
                                         min_size=20,
                                         max_size=80,
                                         opacity_by='pagerank',
                                         min_opacity=0.3,
                                         max_opacity=0.8,
                                         font_size_by='pagerank',
                                         font_min_size=20,
                                         font_max_size=26,
                                         )

current_student_nodes = format_cyto_nodes(student_node_frame[student_node_frame['entity_subtype'] == 'current_student'],
                                          parent='entity_type',
                                          classes='entity_node student current',
                                          )

alumni_student_nodes = format_cyto_nodes(student_node_frame[student_node_frame['entity_subtype'] == 'alumni'],
                                         parent='entity_type',
                                         classes='entity_node student alumni',
                                         )

student_co_advise_relations = format_cyto_edges(student_edge_frame[student_edge_frame.relationship == 'Co-Advised'],
                                                classes='co_advised_edge student',
                                                size_by='weight',
                                                min_size=5,
                                                max_size=8,
                                                opacity_by='weight',
                                                min_opacity=0.4,
                                                max_opacity=0.6,
                                                font_size_by='weight',
                                                font_min_size=18,
                                                font_max_size=22,
                                                )

# student_co_committee_relations = format_cyto_edges(
#     student_edge_frame[student_edge_frame.relationship == 'Co-Committee'],
#     classes='co_committee_edge student',
#     size_by='weight',
#     min_size=3,
#     max_size=6,
#     opacity_by='weight',
#     min_opacity=0.3,
#     max_opacity=0.6,
#     font_size_by='weight',
#     font_min_size=12,
#     font_max_size=16,
# )

bipartite_edge_frame = pd.read_csv(ROOT_DIR + '/data/app/bipartite_edge_frame.csv')
bipartite_edge_frame = pd.merge(bipartite_edge_frame[['source', 'target', 'relationship']],
                                edge_master,
                                on=['source', 'target', 'relationship'],
                                how='inner'
                                )
# print(bipartite_edge_frame.head())

bipartite_advisor_relations = format_cyto_edges(
    bipartite_edge_frame[bipartite_edge_frame.relationship == 'Advisor'],
    classes='bipartite_advised_edge',
    size_by='weight',
    min_size=4,
    max_size=4,
    opacity_by='weight',
    min_opacity=0.4,
    max_opacity=0.4,
    font_size_by='weight',
    font_min_size=26,
    font_max_size=26,
)

cyto_elements = {
    # faculty
    'entity_root_node faculty': faculty_root_nodes,
    'entity_type_node faculty': faculty_type_nodes,
    'entity_node faculty core': core_faculty_nodes,
    'entity_node faculty affiliated': affiliated_faculty_nodes,
    'entity_node faculty related': related_faculty_nodes,
    'entity_node faculty unknown': unknown_faculty_nodes,
    'co_advised_edge faculty': faculty_co_advise_relations,
    'co_committee_edge faculty': faculty_co_committee_relations,
    # Students
    'entity_root_node student': student_root_nodes,
    # 'student_type_node': student_type_nodes,
    'entity_node student current': current_student_nodes,
    'entity_node student alumni': alumni_student_nodes,
    'co_advised_edge student': student_co_advise_relations,
    # 'student_co_committee_edge': student_co_committee_relations,
    # Bipartite Edges
    'bipartite_advised_edge': bipartite_advisor_relations
}

###
flatten = lambda l: list(reduce(lambda a, b: a + b, l))

orig_root_nodes = flatten([cyto_elements[cls] for cls in cyto_elements if 'entity_root_node' in cls])
orig_type_nodes = flatten([cyto_elements[cls] for cls in cyto_elements if 'entity_type_node' in cls])
orig_entity_nodes = flatten([cyto_elements[cls] for cls in cyto_elements if 'entity_node' in cls])
orig_filter_edges = flatten([cyto_elements[cls] for cls in cyto_elements if cls in FILTERABLE_EDGE_CLASSES])
max_weight = {e_type: max([ele['data']['weight'] for ele in orig_filter_edges if e_type in ele['classes']])
              for e_type in ['co_advised_edge', 'co_committee_edge']
              }
orig_bipartite_edges = flatten([cyto_elements[cls] for cls in cyto_elements if cls in ['bipartite_advised_edge']])
