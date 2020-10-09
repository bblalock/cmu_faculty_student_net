import dash_html_components as html
from layout import get_layout
from callbacks import *

app.title = 'CMU NET'
app.layout = html.Div(children=get_layout(cyto_elements))

server = app.server

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
