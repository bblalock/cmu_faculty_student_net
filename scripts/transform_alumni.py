import pandas as pd
from constants import ROOT_DIR

if __name__ == "__main__":
    alumni_phd = pd.read_csv(ROOT_DIR + '/data/scraped/alumni_phd.csv')
    current_students = pd.read_csv(ROOT_DIR + '/data/transformed/current_student_nodes.csv')
    current_students['entity_type'] = 'student'
    current_students['entity_subtype'] = 'current_student'
    student_master = pd.concat([alumni_phd, current_students.loc[:, ['name', 'entity_type', 'entity_subtype']]]).rename(
        columns={'name': 'id'})
    student_master.to_csv(ROOT_DIR + '/data/transformed/student_master.csv', index=False)

    review_frame = pd.read_csv(ROOT_DIR + '/data/transformed/match_review_frame.csv')
    alumni_faculty_edges = review_frame.loc[
        review_frame.correct_match == 1, ['alumni_match', 'faculty_match', 'correct_role']].reset_index(drop=True)
    alumni_faculty_edges.columns = ['student', 'faculty', 'edge_type']

    current_student_edges = pd.read_csv(ROOT_DIR + '/data/transformed/current_student_edges.csv')
    student_master_edges = pd.concat([alumni_faculty_edges, current_student_edges])
    student_master_edges = student_master_edges.loc[student_master_edges.student != student_master_edges.faculty]
    student_master_edges.to_csv(ROOT_DIR + '/data/transformed/student_faculty_relationships.csv', index=False)

    faculty_master = pd.read_csv(ROOT_DIR + '/data/transformed/faculty_master.csv')
    new_faculty = alumni_faculty_edges.rename(columns={'faculty': 'id'}) # [~alumni_faculty_edges['faculty'].isin(faculty_master.id.tolist())]
    new_faculty['entity_type'] = 'faculty'
    new_faculty['entity_subtype'] = 'unknown'
    new_faculty['title'] = ''
    new_faculty['research_interests'] = ''

    new_faculty = new_faculty[['id', 'entity_type', 'entity_subtype', 'title', 'research_interests']].drop_duplicates()
    faculty_master = pd.concat([faculty_master, new_faculty])
    f = lambda x: pd.factorize(x)[0]
    faculty_master['rank'] = faculty_master.groupby('id')['entity_subtype'].transform(f) + 1
    faculty_master = faculty_master[faculty_master['rank'] == 1]
    faculty_master = faculty_master.drop(columns=['rank'])
    faculty_master.to_csv(ROOT_DIR + '/data/transformed/faculty_master.csv', index=False)

    students_with_no_data = student_master[student_master['entity_subtype']=='alumni']
    students_with_no_data = students_with_no_data[~students_with_no_data['id'].isin(alumni_faculty_edges.student.tolist())][['id']]
    students_with_no_data.to_csv(ROOT_DIR + '/data/transformed/students_with_no_data.csv', index=False)
