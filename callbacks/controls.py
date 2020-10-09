from dash.dependencies import Input, Output, State
from app import app, cyto_elements
from utils.cyto import cyto_network

@app.callback([Output('edge_weight_slider_comm', 'max'),
               Output('edge_weight_slider_comm', 'marks'),
               Output('edge_weight_slider_adv', 'max'),
               Output('edge_weight_slider_adv', 'marks')
               ],
              [Input('cmu_net', 'elements'),
               Input('edge_weight_slider_comm', 'value'),
               Input('edge_weight_slider_adv', 'value'),
               ]
              )
def set_max_edge_weight(elements, comm_value, adv_value):
    max_weight = {e_type: max([ele['data']['weight'] for ele in elements if ele['classes'] == e_type])
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

# @app.callback(Output('cmu_net_loading', 'children'),
#               [Input('node_filter_dropdown', 'value')],
#               [State('cmu_net', 'elements')]
#               )
# def filter_nodes(nodes_to_include, elements):
#     print(nodes_to_include)
#     if not nodes_to_include:
#         return [cyto_network(elements, is_dict=False)]
#     faculty_types = ['core_faculty', 'affiliated_faculty', 'related_faculty', 'unknown_faculty']
#     new_elements = [ele for ele in elements if ele['classes'] != 'faculty_node' and 'edge' != ele['classes']]
#     for item in nodes_to_include:
#         if item == 'faculty':
#             for ftype in faculty_types:
#                 new_elements = new_elements + cyto_elements[ftype]
#         else:
#             new_elements = new_elements + cyto_elements[item]
#     return [cyto_network(new_elements, is_dict=False)]