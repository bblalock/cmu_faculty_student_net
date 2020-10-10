from dash.dependencies import Input, Output, State
from app_setup import app, cyto_elements
from functools import reduce


@app.callback(Output('cmu_net', 'elements'),
              [Input('edge_weight_slider_comm', 'value'),
               Input('edge_weight_slider_adv', 'value'),
               Input('degree_zero_switch', 'on'),
               Input('node_filter_dropdown', 'value'),
               ],
              [State('cmu_net', 'elements')]
              )
def filter_graph(weight_filter_comm, weight_filter_adv,
                 degree_switch, nodes_to_include,
                 elements
                 ):
    edge_types = ['co_advised_edge', 'co_committee_edge']

    weight_filter = {'co_advised_edge': weight_filter_adv,
                     'co_committee_edge': weight_filter_comm
                     }

    min_weight = {e_type: min([ele['data']['weight'] for ele in elements if e_type in ele['classes']])
                  for e_type in edge_types
                  }

    import numpy as np
    orig_elements = list(reduce(lambda a, b: a + b, cyto_elements.values()))
    nodes = [ele for ele in orig_elements
             if 'entity_node' in ele['classes']
             ]

    edges = []
    for e_type in edge_types:
        if weight_filter[e_type] < min_weight[e_type]:
            edge = [ele for ele in orig_elements
                    if e_type in ele['classes'] and ele['data']['weight'] >= weight_filter[e_type]  # and ele in edges
                    ]
        else:
            edge = [ele for ele in elements
                    if e_type in ele['classes'] and ele['data']['weight'] >= weight_filter[e_type]  # and ele in edges
                    ]
        edges = edges + edge

    # I need the bipartite edges to still be here so connected components will not float away in the layout
    # if (np.any(['faculty' in _ for _ in nodes_to_include])) & (np.any(['student' in _ for _ in nodes_to_include])):
    bipartite_edges = [ele for ele in orig_elements
                       if ele['classes'] == 'advised_edge'
                       ]
    edges = edges + bipartite_edges

    non_zero_degree_nodes = set(list(reduce(lambda a, b: a + b,
                                            [
                                                [e['data']['source'], e['data']['target']]
                                                for e in edges
                                            ]
                                            )
                                     )
                                )

    for node in nodes:
        if 'entity_node' in node['classes']:
            if node['classes'].split(' ')[1] in nodes_to_include:
                if node['data']['id'] not in non_zero_degree_nodes:
                    if degree_switch:
                        node['data']['display'] = 'element'
                    else:
                        node['data']['display'] = 'none'
                else:
                    node['data']['display'] = 'element'
            else:
                node['data']['display'] = 'none'
        else:
            node['data']['display'] = 'element'

    root_nodes = [ele for ele in orig_elements
                  if 'entity_root_node' in ele['classes']
                  ]

    type_nodes = [ele for ele in orig_elements
                  if 'entity_type_node' in ele['classes']
                  ]

    cmp_root_nodes = root_nodes
    cmp_type_nodes = type_nodes

    return cmp_root_nodes + cmp_type_nodes + nodes + edges
