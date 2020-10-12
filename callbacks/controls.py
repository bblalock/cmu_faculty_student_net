from dash.dependencies import Input, Output, State
from app_setup import app


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

    marks = {'co_advised_edge': {0: {'label': '0', 'style': {'color': 'white'}},
                                 adv_value: {'label': str(adv_value), 'style': {'color': 'white'}},
                                 max_weight['co_advised_edge']: {'label': str(max_weight['co_advised_edge']),
                                                                 'style': {'color': 'white'}}
                                 },
             'co_committee_edge': {0: {'label': '0', 'style': {'color': 'white'}},
                                   comm_value: {'label': str(comm_value), 'style': {'color': 'white'}},
                                   max_weight['co_committee_edge']: {'label': str(max_weight['co_committee_edge']),
                                                                     'style': {'color': 'white'}}
                                   }
             }

    return [max_weight['co_committee_edge'], marks['co_committee_edge'],
            max_weight['co_advised_edge'], marks['co_advised_edge'],
            ]
