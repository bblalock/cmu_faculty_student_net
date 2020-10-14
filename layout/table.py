import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

from utils.cond_format import data_bars, community_colors


def initialize_tables(node_master):
    faculty_df = node_master[node_master['entity_type'] == 'faculty']
    faculty_df = faculty_df[['id', 'entity_subtype', 'community', 'degree', 'pagerank']] \
        .rename(columns={'id': 'Name',
                         'entity_subtype': 'Type',
                         'community': 'Community',
                         'degree': 'Degree',
                         'pagerank': 'Pagerank'
                         }
                )\
        .sort_values(['Degree'], ascending=False)

    student_df = node_master[node_master['entity_type'] == 'student']
    student_df = student_df[['id', 'entity_subtype', 'community', 'degree', 'pagerank']] \
        .rename(columns={'id': 'Name',
                         'entity_subtype': 'Type',
                         'community': 'Community',
                         'degree': 'Degree',
                         'pagerank': 'Pagerank'
                         }
                )\
        .sort_values(['Degree'], ascending=False)

    community_color_dict = node_master[['community', 'community_color']].drop_duplicates()
    community_color_dict = community_color_dict.set_index('community').to_dict('index')

    children = [
        html.Div(
            [
                html.Div(
                    [
                        dbc.CardHeader(html.H4("Faculty Members", className="card-title")),
                        dash_table.DataTable(
                            id='faculty_table',
                            columns=[{"name": i, "id": i,
                                      "deletable": False, "selectable": True
                                      }
                                     for i in faculty_df.columns
                                     ],
                            data=faculty_df.to_dict(
                                'records'),
                            style_table={'overflowX': 'auto',
                                         'minWidth': '100%',
                                         'overflowY': 'auto',
                                         'height': 400,
                                         },
                            style_as_list_view=False,
                            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                            style_cell={
                                'backgroundColor': 'rgb(50, 50, 50)',
                                'color': 'white'
                            },
                            style_data_conditional=(
                                    community_colors(community_color_dict) +
                                    data_bars(faculty_df, 'Degree') +
                                    data_bars(faculty_df, 'Pagerank')
                            ),
                            column_selectable=False,
                            row_selectable=False,
                            row_deletable=False,
                            css=[{'selector': '.row', 'rule': 'margin: 0'}],
                            page_current=0,
                            page_size=20,
                            page_action='native',
                            filter_action='native',
                            sort_action='native',  # custom
                            sort_mode='multi',
                        )
                    ],
                    className='pretty_container card',
                )
            ],
            className='entity_table col-6',
            style={'display': 'inline-block'}
        ),
        html.Div(
            [
                html.Div(
                    [
                        dbc.CardHeader(html.H4("Students", className="card-title")),
                        dash_table.DataTable(
                            id='students_table',
                            columns=[{"name": i, "id": i,
                                      "deletable": False, "selectable": True
                                      }
                                     for i in student_df.columns
                                     ],
                            data=student_df.sort_values(['Degree'], ascending=False).to_dict(
                                'records'),
                            style_table={'overflowX': 'auto',
                                         'minWidth': '100%',
                                         'overflowY': 'auto',
                                         'height': 400,
                                         },
                            style_as_list_view=False,
                            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                            style_cell={
                                'backgroundColor': 'rgb(50, 50, 50)',
                                'color': 'white'
                            },
                            style_data_conditional=(
                                    community_colors(community_color_dict) +
                                    data_bars(student_df, 'Degree') +
                                    data_bars(student_df, 'Pagerank')
                            ),
                            column_selectable=False,
                            row_selectable=False,
                            row_deletable=False,
                            css=[{'selector': '.row', 'rule': 'margin: 0'}],
                            page_current=0,
                            page_size=20,
                            page_action='native',
                            filter_action='native',
                            sort_action='native',  # custom
                            sort_mode='multi',
                        )
                    ],
                    className='pretty_container card',
                )
            ],
            className='entity_table col-6',
            style={'display': 'inline-block'}
        )
    ]

    return children
