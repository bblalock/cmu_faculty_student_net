import pandas as pd
from constants import ROOT_DIR

if __name__ == "__main__":
    alumni_phd = pd.read_csv(ROOT_DIR + '/data/scraped/alumni_phd.csv')
    current_students = pd.read_csv(ROOT_DIR + '/data/transformed/current_student_nodes.csv')
    current_students['entity_type'] = 'current_student'
    student_master = pd.concat([alumni_phd, current_students.loc[:, ['name', 'entity_type']]])
    student_master.to_csv(ROOT_DIR+'/data/transformed/student_master.csv', index=False)

    review_frame = pd.read_csv(ROOT_DIR+'/data/transformed/match_review_frame.csv')
    alumni_faculty_edges = review_frame.loc[
        review_frame.correct_match == 1, ['alumni_match', 'faculty_match', 'correct_role']].reset_index(drop=True)
    alumni_faculty_edges.columns = ['student', 'faculty', 'edge_type']

    current_student_edges = pd.read_csv(ROOT_DIR+'/data/transformed/current_student_edges.csv')
    student_master_edges = pd.concat([alumni_faculty_edges, current_student_edges])
    student_master_edges = student_master_edges.loc[student_master_edges.student != student_master_edges.faculty]
    student_master_edges.to_csv(ROOT_DIR+'/data/transformed/student_faculty_relationships.csv', index=False)