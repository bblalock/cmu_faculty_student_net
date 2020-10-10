from constants import DEFAULT_STYLESHEET
from dash.dependencies import Input, Output
from app_setup import app


@app.callback(Output('cmu_net', 'stylesheet'),
              [Input('cmu_net', 'tapNode'),
               # Input('degree_zero_switch', 'on')
               ]
              )
def generate_stylesheet(node):
    if node and ('entity_node' in node['classes']):
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
                'style': {'content': 'data(label)',
                          'font-size': '50px',
                          'text-transform': 'uppercase',
                          'compound-sizing-wrt-labels': 'include',
                          "background-opacity": 0.0
                          }
            },
            {
                'selector': '.entity_type_node',
                'style': {'content': 'data(label)',
                          'font-size': '30px',
                          'text-transform': 'uppercase',
                          'compound-sizing-wrt-labels': 'include',
                          "background-opacity": 0.2
                          }
            },
            {
                'selector': '.entity_node',
                'style': {'background-opacity': 0.1,
                          }
            },
            {
                'selector': '.co_advised_edge',
                'style': {'opacity': 0.1,
                          'curve-style': 'bezier',
                          }
            },
            {
                'selector': '.co_committee_edge',
                'style': {'opacity': 0.1,
                          'curve-style': 'bezier',
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
                    "border-width": 2,
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
                if edge['relationship'] == 'Co-Advised':
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
                    }
                })

        stylesheet_dict = {selector['selector']: selector for selector in stylesheet}
    else:
        stylesheet_dict = {selector['selector']: selector for selector in DEFAULT_STYLESHEET}

    stylesheet_dict['.entity_node']['style']['display'] = 'data(display)'
    # if degree_switch:
    #     stylesheet_dict['.entity_node']['style']['display'] = 'data(display)'
    # else:
    #     stylesheet_dict['.entity_node']['style']['display'] = 'data(display)'

    return list(stylesheet_dict.values())
