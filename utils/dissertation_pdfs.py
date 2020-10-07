from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from functools import reduce
from utils import clean_line, get_top_matches
import re


def strip_page_stop_words(s):
    tokens = word_tokenize(s)
    return [word for word in tokens if word not in stopwords.words()]


def scrape_dissertation_page(page, alumni_list, faculty_list):
    if page['text'] == 'ERROR':
        return {'alumni_match': None,
                'alumni_compared_line': None,
                'faculty_matches': None
                }

    page = [line for line in re.split('; |, |\*|\n', page['text']) if line not in ['', None]]

    cleaned_lines = []
    for line in page:
        line = strip_page_stop_words(line)
        if len(line) > 0:
            line = reduce(lambda a, b: a + ' ' + b, line)
            cleaned_lines.append(line)

    page = cleaned_lines
    committee_index = next((i for i, line in enumerate(page) if 'committee' in clean_line(line)), 0)

    alumni_matches = get_top_matches(page, alumni_list, normalize_func=lambda i: i)
    faculty_matches = get_top_matches(page[committee_index + 1:], faculty_list, normalize_func=lambda i: i)

    alumni_matches = [tup for tup in alumni_matches if tup[2] >= 0.90]
    faculty_matches = [tup for tup in faculty_matches if tup[2] >= 0.90]

    if len(alumni_matches):
        compared_line = reduce(lambda a, b: str(a) + ' ' + str(b),
                               [tup[0]
                                for tup
                                in alumni_matches
                                if tup[2] >= 0.90
                                ]
                               )

        alumni_matches = [tup[1]
                          for tup
                          in alumni_matches
                          ]
    else:
        compared_line = None
        alumni_matches = None

    if len(faculty_matches):
        faculty_matches = [[tup[1], 'Chair']
                           if (i == 0) or ('chair' in tup[0].lower())
                           else [tup[1], 'Non-chair']
                           for i, tup
                           in enumerate(faculty_matches)
                           ]
    else:
        faculty_matches = None

    return {'alumni_match': alumni_matches,
            'alumni_compared_line': compared_line,
            'faculty_matches': faculty_matches
            }


def scrape_dissertation_pages(page_list, alumni_list, faculty_list):
    for i, page in enumerate(page_list):
        page = {**page, **scrape_dissertation_page(page, alumni_list, faculty_list)}
        page_list[i] = page
    return page_list
