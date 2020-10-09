from dash.dependencies import Input, Output, State
from app import app, cyto_elements
from functools import reduce


@app.callback(Output('cmu_net', 'elements'),
              [Input('edge_weight_slider_comm', 'value'),
               Input('edge_weight_slider_adv', 'value'),
               Input('degree_zero_switch', 'on'),
               Input('node_filter_dropdown', 'value')
               ],
              [State('cmu_net', 'elements')]
              )
def filter_graph(weight_filter_comm, weight_filter_adv, degree_switch, nodes_to_include, elements):
    edge_types = ['co_advised_edge', 'co_committee_edge']

    weight_filter = {'co_advised_edge': weight_filter_adv,
                     'co_committee_edge': weight_filter_comm
                     }

    min_weight = {e_type: min([ele['data']['weight'] for ele in elements if ele['classes'] == e_type])
                  for e_type in edge_types
                  }

    orig_elements = list(reduce(lambda a, b: a + b, cyto_elements.values()))
    nodes = [ele for ele in orig_elements
             if 'edge' not in ele['classes']

             ]

    edges = []
    for e_type in edge_types:
        if weight_filter[e_type] < min_weight[e_type]:
            edge = [ele for ele in orig_elements
                    if ele['classes'] == e_type and ele['data']['weight'] >= weight_filter[e_type]
                    ]
        else:
            edge = [ele for ele in elements
                    if ele['classes'] == e_type and ele['data']['weight'] >= weight_filter[e_type]
                    ]
        edges = edges + edge

    non_zero_degree_nodes = set(list(reduce(lambda a, b: a + b,
                                            [
                                                [e['data']['source'], e['data']['target']]
                                                for e in edges
                                            ]
                                            )
                                     )
                                )

    for node in nodes:
        if 'faculty_node' in node['classes']:
            if node['classes'].split(' ')[1] in nodes_to_include:
                if degree_switch or node['data']['id'] in non_zero_degree_nodes:
                    node['data']['display'] = 'element'
                else:
                    node['data']['display'] = 'none'
            else:
                node['data']['display'] = 'none'
        else:
            node['data']['display'] = 'element'

    return nodes + edges
