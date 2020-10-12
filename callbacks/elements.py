from dash.dependencies import Input, Output, State
from app_setup import app, orig_filter_edges, orig_bipartite_edges, orig_entity_nodes, orig_root_nodes, orig_type_nodes
from functools import reduce
import numpy as np
from constants import FILTERABLE_EDGE_CLASSES


def filter_edges_by_weight(current_elements,
                           weight_filter_adv, weight_filter_comm,
                           nodes_to_include
                           ):
    weight_filters = {cls: weight_filter_adv if 'advis' in cls else weight_filter_comm
                      for cls in FILTERABLE_EDGE_CLASSES
                      }

    current_filterable_edges = [ele for ele in current_elements if ele['classes'] in FILTERABLE_EDGE_CLASSES]

    min_weight = {e_type: min([ele['data']['weight']
                               for ele in current_filterable_edges
                               if ele['classes'] == e_type
                               ]
                              )
                  for e_type in FILTERABLE_EDGE_CLASSES
                  }

    edges = []
    for e_type in FILTERABLE_EDGE_CLASSES:
        if weight_filters[e_type] < min_weight[e_type]:
            edge = [ele for ele in orig_filter_edges
                    if ele['classes'] == e_type and ele['data']['weight'] >= weight_filters[e_type]
                    ]
        else:
            edge = [ele for ele in current_filterable_edges
                    if ele['classes'] == e_type and ele['data']['weight'] >= weight_filters[e_type]
                    ]
        edges = edges + edge

    if (np.any(['faculty' in _ for _ in nodes_to_include])) & (np.any(['student' in _ for _ in nodes_to_include])):
        bipartite_edges = orig_bipartite_edges
        edges = edges + bipartite_edges

    return edges


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
    edges = filter_edges_by_weight(current_elements=elements,
                                   weight_filter_adv=weight_filter_adv,
                                   weight_filter_comm=weight_filter_comm,
                                   nodes_to_include=nodes_to_include
                                   )

    nodes = orig_entity_nodes

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
            if node['classes'] in nodes_to_include:
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

    return orig_root_nodes + orig_type_nodes + nodes + edges
