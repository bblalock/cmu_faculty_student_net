def data_bars(df, column):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    ranges = [
        ((df[column].max() - df[column].min()) * i) + df[column].min()
        for i in bounds
    ]

    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        max_bound_percentage = bounds[i] * 100

        styles.append({
            'if': {
                'filter_query': ('{{{column}}} >= {min_bound}' +
                                 (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                                 ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'background': (
                """
                linear-gradient(90deg, 
                rgb(0, 0, 0) 0%, 
                rgb(0, 0, 0) {max_bound_percentage}%, 
                rgb(50, 50, 50) {max_bound_percentage}%, 
                rgb(50, 50, 50) 100%)""".format(max_bound_percentage=max_bound_percentage)
            ),
            'paddingBottom': 2,
            'paddingTop': 2
        })

    return styles


def community_colors(community_color_dict):
    styles = []
    for community in community_color_dict:
        styles.append({
            'if': {
                'filter_query': '{{{col}}} = {value}'.format(col='Community', value=community),
                'column_id': 'Community'
            },
            'backgroundColor': community_color_dict[community]['community_color'],

        })

    return styles


def create_community_color_dict(node_master):
    community_color_dict = node_master[['community', 'community_color']].drop_duplicates()
    community_color_dict = community_color_dict.set_index('community').to_dict('index')
    return community_color_dict


def create_faculty_student_table_dfs(node_master):
    faculty_df = node_master[node_master['entity_type'] == 'faculty']
    faculty_df = faculty_df[['id', 'entity_subtype', 'community', 'degree', 'pagerank']] \
        .rename(columns={'id': 'Name',
                         'entity_subtype': 'Type',
                         'community': 'Community',
                         'degree': 'Degree',
                         'pagerank': 'Pagerank'
                         }
                ) \
        .sort_values(['Degree'], ascending=False)

    student_df = node_master[node_master['entity_type'] == 'student']
    student_df = student_df[['id', 'entity_subtype', 'community', 'degree', 'pagerank']] \
        .rename(columns={'id': 'Name',
                         'entity_subtype': 'Type',
                         'community': 'Community',
                         'degree': 'Degree',
                         'pagerank': 'Pagerank'
                         }
                ) \
        .sort_values(['Degree'], ascending=False)

    return faculty_df, student_df
