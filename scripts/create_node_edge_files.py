import pandas as pd
from constants import ROOT_DIR
from utils.network import cooccurrence_edgelist, get_node_edge_frame

if __name__ == "__main__":
    student_faculty_connections = pd.read_csv(ROOT_DIR + '/data/transformed/student_faculty_relationships.csv').dropna()

    bipartite_edges = student_faculty_connections.rename(
        columns={'student': 'target', 'faculty': 'source', 'edge_type': 'relationship'})

    bipartite_edges['weight'] = 1

    bipartite_edges = bipartite_edges[['source', 'target', 'weight', 'relationship']]

    bipartite_edges.to_csv(ROOT_DIR + '/data/app/bipartite_edge_frame.csv', index=False)
    bipartite_edges = pd.read_csv(ROOT_DIR + '/data/app/bipartite_edge_frame.csv')

    ########################
    # Co-Occurrence Graphs #
    ########################
    faculty_cooccurrence = cooccurrence_edgelist(student_faculty_connections, on='student').dropna()
    faculty_cooccurrence = faculty_cooccurrence[(faculty_cooccurrence['relationship'] == 'Co-Advised') |
                                                ((faculty_cooccurrence['weight'] > 2) &
                                                 (faculty_cooccurrence['relationship'] == 'Co-Committee')
                                                 )
                                                ].dropna()

    student_cooccurrence = cooccurrence_edgelist(student_faculty_connections, on='faculty')
    student_cooccurrence = student_cooccurrence[(student_cooccurrence['relationship'] == 'Co-Advised') &
                                                (student_cooccurrence['weight'] > 0)
                                                ].dropna()
    # student_cooccurrence = student_cooccurrence[student_cooccurrence.relationship == 'Co-Advised']

    #################
    # Faculty Graph #
    #################
    faculty_master = pd.read_csv(ROOT_DIR + '/data/transformed/faculty_master.csv')
    faculty_master = faculty_master[['id', 'entity_type', 'entity_subtype']].drop_duplicates()

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
    student_master = student_master[['id', 'entity_type', 'entity_subtype']].drop_duplicates()

    student_node_frame, student_edge_frame = get_node_edge_frame(student_master,
                                                                 student_cooccurrence,
                                                                 # name_prefix='student_'
                                                                 )

    student_node_frame.to_csv(ROOT_DIR + '/data/app/student_node_frame.csv', index=False)
    student_edge_frame.to_csv(ROOT_DIR + '/data/app/student_edge_frame.csv', index=False)

    ################
    # Master Graph #
    ################
    node_master = pd.concat([faculty_master, student_master]).drop_duplicates().reset_index(drop=True)
    edge_master = pd.concat(
        [
            faculty_cooccurrence,
            student_cooccurrence[student_cooccurrence['relationship'] == 'Co-Advised'],
            bipartite_edges[bipartite_edges.relationship == 'Advisor']
        ]
    ).drop_duplicates().reset_index(drop=True)
    # print(edge_master[edge_master['source'] == 'Manuela Veloso'])

    f = lambda x: pd.factorize(sorted(x))[0]
    node_master['rank'] = node_master.groupby('id', sort=True)['entity_type'].transform(f) + 1
    node_master = node_master[node_master['rank'] == 1]
    node_master = node_master.drop(columns=['rank'])

    node_master, edge_master = get_node_edge_frame(node_df=node_master,
                                                   edgelist_df=edge_master,
                                                   # name_prefix='faculty_'
                                                   )

    # print(edge_master[edge_master['source'] == 'Manuela Veloso'])

    # print(edge_master.head())
    # edge_master = pd.merge(edge_master,
    #                        faculty_edge_frame[['source', 'target', 'relationship']],
    #
    #                        )
    # print(edge_master.head())

    node_master.to_csv(ROOT_DIR + '/data/app/master_node_frame.csv', index=False)
    edge_master.to_csv(ROOT_DIR + '/data/app/master_edge_frame.csv', index=False)
