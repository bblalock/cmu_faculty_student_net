import dash_html_components as html
from layout import get_layout
from callbacks import *
from app_setup import cyto_elements, node_master

server = app.server
app.title = 'CMU NET'
app.layout = html.Div(children=get_layout(cyto_elements, node_master))

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
