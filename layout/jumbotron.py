import dash_html_components as html
import dash_core_components as dcc


def get_selector():
    selector = [html.Hr(className="my-2"),
                html.P(
                    [
                        "Run this report for: ",
                    ]
                ),
                dcc.Dropdown(
                    id="test_dropdown",
                    options=
                    [
                        {
                            "label": "All",
                            "value": "All",
                        },
                    ] +
                    [
                        {
                            "label": "Not All",
                            "value": _
                        }
                        for _ in [1, 2, 3, 4]
                    ],
                    value='All',
                    multi=False,
                    clearable=False,
                )
                ]

    return selector


def get_children():
    children = html.Div(
        [
            html.H1(
                "CMU NET",
                className="display-5",
            ),
            html.P(
                [
                    "",
                    html.Br(),
                    html.Br(),
                ],
                className="lead",
            )
        ],
        id='jumbo_children'
    )
    return [children]


def initialize_jumbo_children():
    return get_children() + get_selector()

