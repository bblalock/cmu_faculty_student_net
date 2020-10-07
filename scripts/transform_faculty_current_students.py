import pandas as pd
import numpy as np
import re
from utils import get_top_matches
from constants import ROOT_DIR

if __name__ == "__main__":
    ## FACULTY
    core_faculty = pd.read_csv(ROOT_DIR + '/data/scraped/core_faculty.csv')

    affiliated_faculty = pd.read_csv(ROOT_DIR + '/data/scraped/affiliated_faculty.csv')
    affiliated_faculty['research_interests'] = np.nan

    related_faculty = pd.read_csv(ROOT_DIR + '/data/scraped/related_faculty.csv')
    related_faculty['research_interests'] = np.nan

    faculty_master = pd.concat([core_faculty, affiliated_faculty, related_faculty])
    faculty_master_list = faculty_master.name.tolist()

    ## CURRENT STUDENTS
    current_phd_students = pd.read_csv(ROOT_DIR + '/data/scraped/current_phd_students.csv')
    current_phd_students['advisor'] = current_phd_students.advisor.str.split(',')
    current_phd_students = current_phd_students.explode('advisor')
    current_phd_students['advisor'] = current_phd_students.advisor.apply(
        lambda x: re.sub('(\(.+?\))', '', str(x).strip()))
    current_phd_students.loc[current_phd_students.advisor == 'nan', 'advisor'] = None
    current_phd_students['match'] = (current_phd_students
                                     .advisor
                                     .apply(lambda x: [tup[1] for tup
                                                       in get_top_matches([str(x)], faculty_master_list,
                                                                          normalize_func=lambda i: i)
                                                       if (tup[2] >= .9)
                                                       ]
                                            )
                                     )
    current_phd_students = current_phd_students.explode('match')

    advisors_not_in_faculty_master = current_phd_students.loc[
        (current_phd_students.match.isna()) & (current_phd_students.advisor.notna()), ['advisor']]
    advisors_not_in_faculty_master.columns = ['name']
    advisors_not_in_faculty_master['entity_type'] = 'faculty'
    advisors_not_in_faculty_master['faculty_type'] = 'unknown'
    advisors_not_in_faculty_master['title'] = np.nan
    advisors_not_in_faculty_master['research_interests'] = np.nan
    advisors_not_in_faculty_master = advisors_not_in_faculty_master[
        ['entity_type', 'faculty_type', 'name', 'title', 'research_interests']]

    faculty_master = pd.concat([faculty_master, advisors_not_in_faculty_master])
    faculty_master = faculty_master[['name', 'entity_type', 'faculty_type', 'title', 'research_interests']].rename(columns={'name':'id'})

    current_phd_students['match'] = current_phd_students.match.combine_first(current_phd_students.advisor)

    current_students_node_frame = current_phd_students.loc[:,
                                  ['name', 'education', 'research_interests']].drop_duplicates()
    current_students_edge_frame = current_phd_students.loc[:, ['name', 'match']].drop_duplicates()
    current_students_edge_frame.columns = ['student', 'faculty']
    current_students_edge_frame['edge_type'] = 'Advisor'

    ## WRITE FILES
    faculty_master.to_csv(ROOT_DIR+'/data/transformed/faculty_master.csv', index=False)
    current_students_node_frame.to_csv(ROOT_DIR + '/data/transformed/current_student_nodes.csv', index=False)
    current_students_edge_frame.to_csv(ROOT_DIR + '/data/transformed/current_student_edges.csv', index=False)