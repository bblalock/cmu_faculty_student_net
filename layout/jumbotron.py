import dash_html_components as html

def get_children():
    children = html.Div(
        [
            html.H2(
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
    return get_children()

