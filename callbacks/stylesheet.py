from constants import DEFAULT_STYLESHEET
from dash.dependencies import Input, Output
from app_setup import app
import numpy as np


def get_clicked_node_stylesheet(node):
    stylesheet = [
        {
            'selector': 'node',
            'style': {
                'text-transform': 'uppercase',
                'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                'font-weight': 700,
                "border-width": 2,
                "border-opacity": 1,
                'color': 'white',
                'content': '',  # No labels
                # 'display': 'data(display)'
            }
        },
        {
            'selector': '.entity_root_node',
            'style': {'compound-sizing-wrt-labels': 'include',
                      'font-size': '50px',
                      "border-color": "white",
                      'background-color': 'white',
                      "background-opacity": 0.0,
                      }
        },
        {
            'selector': '.entity_type_node',
            'style': {'compound-sizing-wrt-labels': 'include',
                      'font-size': '30px',
                      "border-color": "white",
                      'background-color': 'white',
                      "background-opacity": 0.2,
                      }
        },
        {
            'selector': '.entity_node',
            'style': {
                'background-opacity': 0.1,
                'width': 20,
                'background-color': 'grey',
                "border-color": "black",
                "border-width": 0,
                "border-opacity": 0,
            }
        },
        {
            'selector': 'edge',
            'style': {'label': '',  # No Labels
                      'width': 'data(width)',
                      'curve-style': 'bezier',
                      'text-transform': 'uppercase',
                      'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                      'font-weight': 900,
                      'text-opacity': 1,
                      'line-color': "data(community_color)",
                      'color': 'data(community_color)',
                      'opacity': 0.05
                      }
        },
        {
            'selector': '.co_advised_edge',
            'style': {'line-style': 'solid'}
        },
        {
            'selector': '.co_committee_edge',
            'style': {'line-style': 'dashed'}
        },
        {
            'selector': '.bipartite_advised_edge',
            'style': {'line-style': 'solid',
                      'source-arrow-shape': 'tee',
                      'source-arrow-color': 'data(community_color)',
                      'source-arrow-fill': 'filled',
                      'target-arrow-shape': 'triangle',
                      'target-arrow-color': 'data(community_color)',
                      'target-arrow-fill': 'filled',
                      'arrow-scale': 5,
                      }
        },
        {
            "selector": 'node[id = "{}"]'.format(node['data']['id']),
            "style": {
                'content': 'data(label)',
                'width': 'data(size)',
                'height': 'data(size)',
                'font-size': '40px',
                'background-opacity': 'data(opacity)',
                'background-color': 'data(community_color)',
                "border-color": "data(community_color)",
            }
        }
    ]
    for edge in node['edgesData']:
        if edge['source'] == node['data']['id']:
            stylesheet.append({
                "selector": 'node[id = "{}"]'.format(edge['target']),
                "style": {
                    'content': 'data(label)',
                    'width': 'data(size)',
                    'height': 'data(size)',
                    'font-size': 'data(label_size)',
                    'background-opacity': 'data(opacity)',
                    'background-color': 'data(community_color)',
                    "border-color": "data(community_color)",
                    "text-opacity": 1,
                }
            })

            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'label': 'data(relationship)',
                    'width': 'data(width)',
                    'curve-style': 'bezier',
                    'text-transform': 'uppercase',
                    'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                    'font-weight': 900,
                    'text-opacity': 1,
                    'opacity': 1,
                    'line-color': "data(community_color)",
                    'color': 'white',
                    'font-size': 26,
                    'text-outline-color': 'black',
                    'text-outline-opacity': 1,
                    'text-outline-width': 5,
                    'text-rotation': 'autorotate',
                }
            })

            stylesheet.append({
                "selector": '.co_advised_edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'line-style': 'solid'
                }
            })

            stylesheet.append({
                "selector": '.co_committee_edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'line-style': 'dashed'
                }
            })

            stylesheet.append({
                "selector": '.bipartite_advised_edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'line-style': 'solid',
                    'source-arrow-shape': 'tee',
                    'source-arrow-color': 'data(community_color)',
                    'source-arrow-fill': 'filled',
                    'target-arrow-shape': 'triangle',
                    'target-arrow-color': 'data(community_color)',
                    'target-arrow-fill': 'filled',
                    'arrow-scale': 5,
                }
            })
        if edge['target'] == node['data']['id']:
            stylesheet.append({
                "selector": 'node[id = "{}"]'.format(edge['source']),
                "style": {
                    'content': 'data(label)',
                    'width': 'data(size)',
                    'height': 'data(size)',
                    'font-size': 'data(label_size)',
                    'background-opacity': 'data(opacity)',
                    'background-color': 'data(community_color)',
                    "border-color": "data(community_color)",
                    "text-opacity": 1,
                }
            })
            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'label': 'data(relationship)',
                    'width': 'data(width)',
                    'curve-style': 'bezier',
                    'text-transform': 'uppercase',
                    'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                    'font-weight': 900,
                    'text-opacity': 1,
                    'opacity': 1,
                    'line-color': "data(community_color)",
                    'color': 'white',
                    'font-size': 26,
                    'text-outline-color': 'black',
                    'text-outline-opacity': 1,
                    'text-outline-width': 5,
                    'text-rotation': 'autorotate',
                }
            })

            stylesheet.append({
                "selector": '.co_advised_edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'line-style': 'solid'
                }
            })

            stylesheet.append({
                "selector": '.co_committee_edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'line-style': 'dashed'
                }
            })

            stylesheet.append({
                "selector": '.bipartite_advised_edge[id= "{}"]'.format(edge['id']),
                "style": {
                    'line-style': 'solid',
                    'source-arrow-shape': 'tee',
                    'source-arrow-color': 'data(community_color)',
                    'source-arrow-fill': 'filled',
                    'target-arrow-shape': 'triangle',
                    'target-arrow-color': 'data(community_color)',
                    'target-arrow-fill': 'filled',
                    'arrow-scale': 5,
                }
            })

    return stylesheet


@app.callback(Output('cmu_net', 'stylesheet'),
              [Input('cmu_net', 'tapNode'),
               Input('node_filter_dropdown', 'value'),
               ]
              )
def generate_stylesheet(node, nodes_to_include):
    stylesheet = DEFAULT_STYLESHEET

    if node and not node['selected']:
        if ('entity_node' in node['classes']):
            stylesheet = get_clicked_node_stylesheet(node)

    for entity_type in ['faculty', 'student']:
        if not np.any([entity_type in _ for _ in nodes_to_include]):
            stylesheet.append(
                {
                    'selector': '.entity_root_node.{}'.format(entity_type),
                    'style': {
                        'border-width': 0,
                        'border-opacity': 0,
                        'content': '',
                        'display': 'none'

                    }
                }
            )
        else:
            stylesheet.append(
                {
                    'selector': '.entity_root_node.{}'.format(entity_type),
                    'style': {
                        'border-width': 2,
                        'border-opacity': 1,
                        'content': 'data(label)',
                        'display': 'element'

                    }
                }
            )


    for fac_type in ['core', 'affiliated', 'related', 'unknown']:
        if not np.any(['entity_node faculty {}'.format(fac_type) == _ for _ in nodes_to_include]):
            stylesheet.append(
                {
                    'selector': '.entity_type_node[id = "{}"]'.format(fac_type),
                    'style': {
                        'border-width': 0,
                        'border-opacity': 0,
                        'content': '',
                        'display': 'none'

                    }
                },
            )
        else:
            stylesheet.append(
                {
                    'selector': '.entity_type_node[id = "{}"]'.format(fac_type),
                    'style': {
                        'border-width': 2,
                        'border-opacity': 1,
                        'content': 'data(label)',
                        'display': 'element'

                    }
                },
            )

    return stylesheet
