from dash.dependencies import Input, Output
from app_setup import app

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