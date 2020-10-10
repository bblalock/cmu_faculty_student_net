import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app_setup import app, cyto_elements
from utils.cyto import cyto_network


@app.callback([Output('edge_weight_slider_comm', 'max'),
               Output('edge_weight_slider_comm', 'marks'),
               Output('edge_weight_slider_adv', 'max'),
               Output('edge_weight_slider_adv', 'marks')
               ],
              [
               Input('edge_weight_slider_comm', 'value'),
               Input('edge_weight_slider_adv', 'value'),
               ],
              [State('cmu_net', 'elements')]
              )
def set_max_edge_weight(comm_value, adv_value, elements):
    max_weight = {e_type: max([ele['data']['weight'] for ele in elements if e_type in ele['classes']])
                  for e_type in ['co_advised_edge', 'co_committee_edge']
                  }

    marks = {'co_advised_edge': {0: {'label': '0', 'style': {'color': 'black'}},
                                 adv_value: {'label': str(adv_value), 'style': {'color': 'black'}},
                                 max_weight['co_advised_edge']: {'label': str(max_weight['co_advised_edge']),
                                                                 'style': {'color': 'black'}}
                                 },
             'co_committee_edge': {0: {'label': '0', 'style': {'color': 'black'}},
                                   comm_value: {'label': str(comm_value), 'style': {'color': 'black'}},
                                   max_weight['co_committee_edge']: {'label': str(max_weight['co_committee_edge']),
                                                                     'style': {'color': 'black'}}
                                   }
             }

    return [max_weight['co_committee_edge'], marks['co_committee_edge'],
            max_weight['co_advised_edge'], marks['co_advised_edge'],
            ]


# @app.callback(Output('cyto_canvas', 'children'),
#               [Input('cmu_net_loading', 'children'),
#                Input('groupby_dropdown', 'value')
#                ]
#               )
# def redraw_graph(children, nodes_to_include):
#     if children:
#         return children
#     else:
#         print(nodes_to_include)
#         if nodes_to_include:
#             if 'entity_type_node' in nodes_to_include:
#                 nodes_to_include = nodes_to_include + ['entity_root_node']
#
#         elements = {ele: cyto_elements[ele]
#                     for ele in
#                     nodes_to_include + ['core_faculty', 'affiliated_faculty', 'related_faculty', 'unknown_faculty',
#                                         'co_advised_edge', 'co_committee_edge'
#                                         ]
#                     }
#         return [dcc.Loading(cyto_network(elements), id='cmu_net_loading')]
#
#
# @app.callback(Output('cmu_net_loading', 'children'),
#               [Input('groupby_dropdown', 'value')],
#               )
# def remove_graph(nodes_to_include):
#     return []
