import copy
import pandas as pd
from constants import ROOT_DIR

if __name__ == "__main__":
    dissertation_abstracts_matches = pd.read_csv(ROOT_DIR + '/data/scraped/dissertation_abstracts_matches.csv')
    dissertation_pdf_matches = pd.read_csv(ROOT_DIR + '/data/scraped/dissertation_pdf_matches.csv')

    dissertation_abstracts_matches['source'] = 'abstract_page'
    dissertation_pdf_matches['source'] = 'dissertation_pdf'
    matches = (pd.concat([dissertation_abstracts_matches, dissertation_pdf_matches])
               .groupby([col for col in dissertation_abstracts_matches.columns
                         if col not in ['source', 'faculty_role']
                         ]
                        )
               .agg(faculty_roles=('faculty_role', 'unique'),
                    sources=('source', 'unique')
                    )
               .reset_index()
               )

    matches['chair'] = matches.faculty_roles.apply(lambda x: 1 if 'Chair' in x else 0)
    matches['faculty_match_num_roles'] = matches.faculty_roles.apply(lambda x: len(x))
    matches['faculty_match_num_sources'] = matches.sources.apply(lambda x: len(x))

    alumni_counts = (copy.deepcopy(matches.reset_index())
                     .groupby(['alumni_match'])
                     .agg(num_chair_matches=('chair', 'sum'),
                          num_faculty_matches=('faculty_match', 'nunique')
                          )
                     .reset_index()
                     )

    review_frame = (pd.merge(alumni_counts, matches, how='inner', on='alumni_match')
                    .sort_values(
        ['num_chair_matches', 'num_faculty_matches', 'alumni_match', 'chair', 'faculty_match_num_sources',
         'faculty_match_num_roles', 'faculty_match'],
        ascending=[False, False, True, False, False, True, True]
    )
                    .reset_index(drop=True)
                    )

    review_frame.index.names = ['review_priority']
    review_frame['correct_match'] = 1
    review_frame['correct_role'] = review_frame.faculty_roles.apply(
        lambda x: 'Advisor' if 'Chair' in x else 'Committee')

    review_frame.to_csv(ROOT_DIR + '/data/transformed/match_review_frame.csv', index=True)
