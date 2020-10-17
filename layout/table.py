import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

from utils.data_table import data_bars, community_colors
from app_setup import faculty_df, student_df, community_color_dict


def initialize_tables():
    children = [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Faculty Members", className="card-title")),
                            dbc.CardBody(
                                [
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
                                ]
                            )
                        ]
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Students", className="card-title")),
                            dbc.CardBody(
                                [
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
                                ]
                            )
                        ]
                    )
                )
            ]
        )

    ]

    return children
