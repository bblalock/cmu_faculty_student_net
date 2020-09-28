import numpy as np
from jellyfish import metaphone, jaro_winkler_similarity
from functools import reduce
import re

stop_words = ['generalized',
              'Pittsburgh',
              'School',
              'Computer',
              'Science',
              'Machine',
              'Learning',
              'Chair',
              'Co-Chair',
              ','
              ]


def strip_stop_words(string):
    stop_word_regex = reduce(lambda a, b: a + '|' + b,
                             [word
                              for word
                              in stop_words
                              ]
                             )
    return re.sub(stop_word_regex, '', string)


def clean_line(line):
    stop_word_regex = reduce(lambda a, b: a + '|' + b,
                             ['\\b' + word.lower() + '\\b'
                              for word
                              in stop_words
                              ]
                             )
    return re.sub('\s|(\(.+?\))|' + stop_word_regex, '', line.lower())


def compare_name_to_line(name, line, normalize_func=metaphone, compare_func=jaro_winkler_similarity):
    name = re.split('\s', name)
    name = (normalize_func(clean_line(name[0])),
            normalize_func(clean_line(name[-1]))
            )

    split_line = re.findall('[A-Z][^A-Z]*', strip_stop_words(line))
    if split_line:
        line = (normalize_func(clean_line(split_line[0])),
                normalize_func(clean_line(split_line[-1]))
                )
    else:
        line = [line]
        line = (normalize_func(clean_line(line[0])),
                normalize_func(clean_line(line[0]))
                )

    return np.average([compare_func(name[i], line[i])
                       for i in range(len(line))
                       ],
                      weights=[1, 2]
                      )


def compare_line_to_names(line, name_list, **kwargs):
    similarities = [(line,
                     name,
                     compare_name_to_line(name, line, **kwargs)
                     )
                    for name in name_list
                    ]

    return similarities


def get_top_match_for_line(line, compare_to_list, **kwargs):
    similarities = compare_line_to_names(line, compare_to_list, **kwargs)
    top_match_for_line = sorted(similarities, key=lambda x: -x[2])[0]
    return top_match_for_line


def get_top_matches(page, compare_list, **kwargs):
    matches = []
    for i, line in enumerate(page):
        matches.append(get_top_match_for_line(line, compare_list, **kwargs))
    return matches
