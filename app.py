import dash
import pandas as pd
import dash_html_components as html
import dash_bootstrap_components as dbc
from constants import DEFAULT_STYLESHEET
from layout import get_layout
from dash.dependencies import Input, Output
pd.set_option('mode.chained_assignment', None)

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.JOURNAL]
                )
app.title = 'CMU NET'
app.layout = html.Div(children=get_layout())

@app.callback(Output('cmu_net', 'stylesheet'),
              [Input('cmu_net', 'tapNode')]
              )
def generate_stylesheet(node):
    if (not node) or (node['classes'] != 'faculty_node'):
        return DEFAULT_STYLESHEET

    stylesheet = [
        {
            'selector': '.faculty_root_node',
            'style': {'content': 'data(label)',
                      'font-size': '50px',
                      'text-transform': 'uppercase',
                      'compound-sizing-wrt-labels': 'include',
                      }
        },
        {
            'selector': '.faculty_type_node',
            'style': {'content': 'data(label)',
                      'font-size': '30px',
                      'text-transform': 'uppercase',
                      'compound-sizing-wrt-labels': 'include',
                      }
        },
        {
            'selector': '.faculty_node',
            'style': {'width': 'data(size)',
                      'height': 'data(size)',
                      'background-opacity': 0.1,
                      }
        },
        {
            'selector': '.co_advised_edge',
            'style': {'line-style': 'solid',
                      'width': 'data(width)',
                      'opacity': 0.1,
                      'curve-style': 'bezier',
                      'line-color': 'blue'
                      }
        },
        {
            'selector': '.co_committee_edge',
            'style': {'line-style': 'dashed',
                      'width': 'data(width)',
                      'opacity': 0.1,
                      'curve-style': 'bezier',
                      'line-color': 'grey'
                      }
        },
        {
            "selector": '.faculty_node[id = "{}"]'.format(node['data']['id']),
            "style": {
                'background-color': '#B10DC9',
                "border-color": "purple",
                "border-width": 2,
                "border-opacity": 1,
                "background-opacity": 0.4,
                "label": "data(label)",
                "text-opacity": 1,
                "font-size": '26px',
                'z-index': 9999
            }
        }
    ]

    for edge in node['edgesData']:
        if edge['source'] == node['data']['id']:
            stylesheet.append({
                "selector": '.faculty_node[id = "{}"]'.format(edge['target']),
                "style": {
                    'background-color': 'blue',
                    'background-opacity': 0.4,
                    "border-color": "blue",
                    "border-width": 2,
                    "border-opacity": 1,
                    "label": "data(label)",
                    "text-opacity": 1,
                    "font-size": '26px'
                }
            })
            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    "line-color": 'purple',
                    'opacity': 0.4,
                }
            })

        if edge['target'] == node['data']['id']:
            stylesheet.append({
                "selector": '.faculty_node[id = "{}"]'.format(edge['source']),
                "style": {
                    'background-color': 'blue',
                    'background-opacity': 0.4,
                    "border-color": "blue",
                    "border-width": 2,
                    "border-opacity": 1,
                    "label": "data(label)",
                    "text-opacity": 1,
                    "font-size": '26px'
                }
            })
            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    "line-color": 'purple',
                    'opacity': 0.4,
                }
            })

    return stylesheet

# Main
if __name__ == "__main__":
    app.run_server(debug=True)