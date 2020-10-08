from dash.dependencies import Input, Output, State
from app import app, cyto_elements


# @app.callback([Output('cmu_net', 'elements')],
#               [Input('degree_zero_switch', 'on')],
#               [State('cmu_net', 'elements')]
#               )
# def zero_degree_switch(switch_on, elements):
#     non_zero_degree_elements = [el for el in elements
#                                 if ('joint_degree' not in el['data']) or (el['data']['joint_degree'] > 0)
#                                 ]
#     zero_degree_elements = [el for el in elements
#                             if ('joint_degree' in el['data']) and (el['data']['joint_degree'] == 0)
#                             ]
#
#     if len(zero_degree_elements) == 0:
#         zero_degree_elements = [el for el in cyto_elements
#                                 if ('joint_degree' in el['data']) and (el['data']['joint_degree'] == 0)
#                                 ]
#
#     if switch_on:
#         return [non_zero_degree_elements + zero_degree_elements]
#     else:
#         return [non_zero_degree_elements]
