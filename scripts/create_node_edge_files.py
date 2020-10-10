import pandas as pd
from constants import ROOT_DIR
from utils.network import cooccurrence_edgelist, get_node_edge_frame

if __name__ == "__main__":
    student_faculty_connections = pd.read_csv(ROOT_DIR + '/data/transformed/student_faculty_relationships.csv')

    bipartite_edges = student_faculty_connections.rename(
        columns={'student': 'target', 'faculty': 'source', 'edge_type': 'relationship'})

    bipartite_edges['weight'] = 1

    bipartite_edges[['source', 'target', 'relationship', 'weight']].to_csv(
        ROOT_DIR + '/data/app/bipartite_edge_frame.csv', index=False)

    ########################
    # Co-Occurrence Graphs #
    ########################
    faculty_cooccurrence = cooccurrence_edgelist(student_faculty_connections, on='student')

    student_cooccurrence = cooccurrence_edgelist(student_faculty_connections, on='faculty')
    student_cooccurrence = student_cooccurrence[(student_cooccurrence['relationship'] == 'Co-Advised') &
                                                (student_cooccurrence['weight'] > 1)
                                                ]
    # student_cooccurrence = student_cooccurrence[student_cooccurrence.relationship == 'Co-Advised']

    #################
    # Faculty Graph #
    #################
    faculty_master = pd.read_csv(ROOT_DIR + '/data/transformed/faculty_master.csv')
    faculty_master['label'] = faculty_master['id']
    faculty_master['parent'] = faculty_master['entity_subtype']
    faculty_master = faculty_master.drop_duplicates()
    faculty_master.head()

    faculty_node_frame, faculty_edge_frame = get_node_edge_frame(faculty_master,
                                                                 faculty_cooccurrence,
                                                                 # name_prefix='faculty_'
                                                                 )

    faculty_node_frame.to_csv(ROOT_DIR + '/data/app/faculty_node_frame.csv', index=False)
    faculty_edge_frame.to_csv(ROOT_DIR + '/data/app/faculty_edge_frame.csv', index=False)

    #################
    # Student Graph #
    #################
    student_master = pd.read_csv(ROOT_DIR + '/data/transformed/student_master.csv')
    student_master['label'] = student_master['id']
    student_master['parent'] = student_master['entity_subtype']
    student_master = student_master.drop_duplicates()
    student_master.head()

    student_node_frame, student_edge_frame = get_node_edge_frame(student_master,
                                                                 student_cooccurrence,
                                                                 # name_prefix='student_'
                                                                 )

    student_node_frame.to_csv(ROOT_DIR + '/data/app/student_node_frame.csv', index=False)
    student_edge_frame.to_csv(ROOT_DIR + '/data/app/student_edge_frame.csv', index=False)
