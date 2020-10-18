import dash
from dash.dependencies import Input, Output, State
from app_setup import app, orig_filter_edges, orig_bipartite_edges, orig_entity_nodes, orig_root_nodes, orig_type_nodes, \
    communities, faculty_df, student_df
from functools import reduce
import numpy as np
from constants import FILTERABLE_EDGE_CLASSES


def filter_edges_by_weight(current_elements,
                           weight_filter_adv,
                           weight_filter_comm,
                           nodes_to_include,
                           ):
    weight_filters = {cls: weight_filter_adv if 'advis' in cls else weight_filter_comm
                      for cls in FILTERABLE_EDGE_CLASSES
                      }

    current_filterable_edges = [ele for ele in current_elements if ele['classes'] in FILTERABLE_EDGE_CLASSES]

    edge_dict = {e_type: [ele['data']['weight']
                          for ele in current_filterable_edges
                          if ele['classes'] == e_type
                          ]
                 for e_type in FILTERABLE_EDGE_CLASSES
                 }

    min_weight = {e_type: min(edge_dict[e_type]) if len(edge_dict[e_type]) > 0 else 99
                  for e_type in edge_dict
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


@app.callback([Output('cmu_net', 'elements'),
               Output('faculty_table', 'data'),
               Output('students_table', 'data'),
               Output('cmu_net', 'autoRefreshLayout')
               ],
              [Input('edge_weight_slider_comm', 'value'),
               Input('edge_weight_slider_adv', 'value'),
               Input('degree_zero_switch', 'on'),
               Input('node_filter_dropdown', 'value'),
               Input('edge_filter_dropdown', 'value'),
               Input('community_dropdown', 'value'),
               Input('redraw_button', 'n_clicks')
               ],
              [State('cmu_net', 'elements')]
              )
def filter_graph(weight_filter_comm, weight_filter_adv,
                 degree_switch,
                 nodes_to_include,
                 edges_to_include,
                 communities_to_include,
                 redraw_clicks,
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

    if 'all' in communities_to_include:
        communities_to_include = communities

    for node in nodes:
        node['data']['display'] = 'element'
        if node['classes'] in nodes_to_include and node['data']['community'] in communities_to_include:
            # if not showing zero degree nodes
            if not degree_switch:
                # if not is zero degree
                if node['data']['id'] not in non_zero_degree_nodes:
                    node['data']['display'] = 'none'
        else:
            node['data']['display'] = 'none'

    node_ids = [node['data']['id'] for node in nodes if node['data']['display'] == 'element']
    faculty_table_data = faculty_df[faculty_df['Name'].isin(node_ids)].sort_values(['Degree'], ascending=False).to_dict(
        'records')
    student_table_data = student_df[student_df['Name'].isin(node_ids)].sort_values(['Degree'], ascending=False).to_dict(
        'records')

    filtered_edges = []
    for edge in edges:
        if edge['classes'] in edges_to_include:
            filtered_edges.append(edge)

    return [orig_root_nodes + orig_type_nodes + nodes + filtered_edges,
            faculty_table_data,
            student_table_data,
            True if [p['prop_id'] for p in dash.callback_context.triggered][0] == 'redraw_button.n_clicks' else False
            ]
