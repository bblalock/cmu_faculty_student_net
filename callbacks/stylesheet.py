from constants import DEFAULT_STYLESHEET
from dash.dependencies import Input, Output
from app_setup import app
import numpy as np


@app.callback(Output('cmu_net', 'stylesheet'),
              [Input('cmu_net', 'tapNode'),
               Input('node_filter_dropdown', 'value'),
               ]
              )
def generate_stylesheet(node, nodes_to_include):
    # print(node)
    if node and not node['selected']:
        if ('entity_node' in node['classes']):
            stylesheet = [
                {
                    'selector': 'node',
                    'style': {
                        'text-transform': 'uppercase',
                        'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                        'font-weight': 700,
                        'color': 'white',
                    }
                },
                {
                    'selector': '.entity_root_node',
                    'style': {
                        'font-size': '50px',
                        'compound-sizing-wrt-labels': 'include',
                        "border-color": "white",
                        'background-color': 'white',
                        "background-opacity": 0.0
                    }
                },
                {
                    'selector': '.entity_root_node.faculty',
                    'style': {
                        'content': 'data(label)',
                        "border-width": 2,
                        "border-opacity": 1,
                    }
                },
                {
                    'selector': '.entity_root_node.student',
                    'style': {
                        'content': 'data(label)',
                        "border-width": 2,
                        "border-opacity": 1,
                    }
                },
                {
                    'selector': '.entity_type_node',
                    'style': {
                        'content': 'data(label)',
                        'font-size': '30px',
                        'text-transform': 'uppercase',
                        'compound-sizing-wrt-labels': 'include',
                        "background-opacity": 0.2
                    }
                },
                {
                    'selector': '.entity_node',
                    'style': {
                        'background-opacity': 0.1,
                    }
                },
                {
                    'selector': 'edge',
                    'style': {'width': 1,
                              'opacity': 0.1,
                              'curve-style': 'bezier',
                              'text-transform': 'uppercase',
                              'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                              'font-weight': 900,
                              'text-opacity': 0.1,
                              'line-color': "data(community_color)",
                              'color': 'data(community_color)',
                              'text-outline-color': "black",
                              'text-outline-opacity': 1,
                              'text-outline-width': 2,
                              'font-size': '24px',
                              'text-rotation': 'autorotate',
                              'label': 'data(relationship)',
                              'min-zoomed-font-size': '36px'
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
                              # 'line-color': "#A9A9A9",
                              # 'color': 'white',
                              }
                },
                {
                    "selector": 'node[id = "{}"]'.format(node['data']['id']),
                    "style": {
                        'content': 'data(label)',
                        'width': 'data(size)',
                        'height': 'data(size)',
                        'font-size': 'data(label_size)',
                        'background-opacity': 'data(opacity)',
                        'background-color': 'data(community_color)',
                        "border-color": "data(community_color)",
                        "border-width": 3,
                        "border-opacity": 1,
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
                            "border-width": 2,
                            "border-opacity": 1,
                            "text-opacity": 1,
                        }
                    })
                    if 'Advis' in edge['relationship']:
                        stylesheet.append({
                            "selector": 'edge[id= "{}"]'.format(edge['id']),
                            "style": {
                                'width': 'data(width)',
                                'curve-style': 'bezier',
                                'line-color': "data(community_color)",
                                'opacity': 0.6,
                                'text-transform': 'uppercase',
                                'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                                'font-weight': 900,
                                'text-opacity': 1,
                                'color': 'data(community_color)',
                                'text-outline-color': "black",
                                'text-outline-opacity': 1,
                                'text-outline-width': 2,
                                'font-size': 'data(label_size)',
                                'text-rotation': 'autorotate',
                                'label': 'data(relationship)',
                                # 'min-zoomed-font-size': '30px'
                            }
                        })
                    else:
                        stylesheet.append({
                            "selector": 'edge[id= "{}"]'.format(edge['id']),
                            "style": {
                                'line-style': 'dashed',
                                'width': 'data(width)',
                                'curve-style': 'bezier',
                                'line-color': "data(community_color)",
                                'opacity': 0.6,
                                'text-transform': 'uppercase',
                                'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                                'font-weight': 900,
                                'text-opacity': 1,
                                'color': 'data(community_color)',
                                'text-outline-color': "black",
                                'text-outline-opacity': 1,
                                'text-outline-width': 2,
                                'font-size': 'data(label_size)',
                                'text-rotation': 'autorotate',
                                'label': 'data(relationship)',
                                # 'min-zoomed-font-size': '30px'
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
                            "border-width": 2,
                            "border-opacity": 1,
                            "text-opacity": 1,
                        }
                    })
                    if 'Advise' in edge['relationship']:
                        stylesheet.append({
                            "selector": 'edge[id= "{}"]'.format(edge['id']),
                            "style": {
                                'width': 'data(width)',
                                'curve-style': 'bezier',
                                'line-color': "data(community_color)",
                                'opacity': 0.6,
                                'text-transform': 'uppercase',
                                'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                                'font-weight': 900,
                                'text-opacity': 1,
                                'color': 'data(community_color)',
                                'text-outline-color': "black",
                                'text-outline-opacity': 1,
                                'text-outline-width': 2,
                                'font-size': 'data(label_size)',
                                'text-rotation': 'autorotate',
                                'label': 'data(relationship)',
                                # 'min-zoomed-font-size': '30px'
                            }
                        })
                    else:
                        stylesheet.append({
                            "selector": 'edge[id= "{}"]'.format(edge['id']),
                            "style": {
                                'line-style': 'dashed',
                                'width': 'data(width)',
                                'curve-style': 'bezier',
                                'line-color': "data(community_color)",
                                'opacity': 0.6,
                                'text-transform': 'uppercase',
                                'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                                'font-weight': 900,
                                'text-opacity': 1,
                                'color': 'data(community_color)',
                                'text-outline-color': "black",
                                'text-outline-opacity': 1,
                                'text-outline-width': 2,
                                'font-size': 'data(label_size)',
                                'text-rotation': 'autorotate',
                                'label': 'data(relationship)',
                                # 'min-zoomed-font-size': '30px'
                            }
                        })

            stylesheet_dict = {selector['selector']: selector for selector in stylesheet}
        else:
            stylesheet_dict = {selector['selector']: selector for selector in DEFAULT_STYLESHEET}
    else:
        stylesheet_dict = {selector['selector']: selector for selector in DEFAULT_STYLESHEET}

    stylesheet_dict['.entity_node']['style']['display'] = 'data(display)'

    if not np.any(['faculty' in _ for _ in nodes_to_include]):
        stylesheet_dict['.entity_root_node.faculty']['style']['border-width'] = 0
        stylesheet_dict['.entity_root_node.faculty']['style']['border-opacity'] = 0
        stylesheet_dict['.entity_root_node.faculty']['style']['content'] = ''
        stylesheet_dict['.entity_root_node.faculty']['style']['visibility'] = 'hidden'
    else:
        stylesheet_dict['.entity_root_node.faculty']['style']['border-width'] = 2
        stylesheet_dict['.entity_root_node.faculty']['style']['border-opacity'] = 1
        stylesheet_dict['.entity_root_node.faculty']['style']['content'] = 'data(label)'
        stylesheet_dict['.entity_root_node.faculty']['style']['visibility'] = 'visible'

    if not np.any(['student' in _ for _ in nodes_to_include]):
        stylesheet_dict['.entity_root_node.student']['style']['border-width'] = 0
        stylesheet_dict['.entity_root_node.student']['style']['border-opacity'] = 0
        stylesheet_dict['.entity_root_node.student']['style']['content'] = ''
        stylesheet_dict['.entity_root_node.student']['style']['visibility'] = 'hidden'
    else:
        stylesheet_dict['.entity_root_node.student']['style']['border-width'] = 2
        stylesheet_dict['.entity_root_node.student']['style']['border-opacity'] = 1
        stylesheet_dict['.entity_root_node.student']['style']['content'] = 'data(label)'
        stylesheet_dict['.entity_root_node.student']['style']['visibility'] = 'visible'

    return list(stylesheet_dict.values())
