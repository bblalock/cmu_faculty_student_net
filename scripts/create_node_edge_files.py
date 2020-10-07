import pandas as pd
from constants import ROOT_DIR
from utils.network import cooccurrence_edgelist, get_node_edge_frame

if __name__ == "__main__":
    ########################
    # Co-Occurrence Graphs #
    ########################
    student_faculty_connections = pd.read_csv(ROOT_DIR + '/data/transformed/student_faculty_relationships.csv')
    faculty_cooccurrence = cooccurrence_edgelist(student_faculty_connections, on='student')
    # student_cooccurrence = cooccurrence_edgelist(student_faculty_connections, on='faculty')
    # student_cooccurrence = [student_cooccurrence.relationship == 'Co-Advised']

    #################
    # Faculty Graph #
    #################
    faculty_master = pd.read_csv(ROOT_DIR + '/data/transformed/faculty_master.csv')
    faculty_master['label'] = faculty_master['id']
    faculty_master['parent'] = faculty_master['faculty_type']
    faculty_master = faculty_master.drop_duplicates()
    faculty_master.head()

    joint_node_frame, joint_edge_frame = get_node_edge_frame(faculty_master,
                                                             faculty_cooccurrence,
                                                             name_prefix='joint'
                                                             )

    joint_node_frame.to_csv(ROOT_DIR + '/data/app/joint_node_frame.csv', index=False)
    joint_edge_frame.to_csv(ROOT_DIR + '/data/app/joint_edge_frame.csv', index=False)
