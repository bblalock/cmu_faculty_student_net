import numpy as np
import dash_cytoscape as cyto
from constants import COSE_BILKENT_LAYOUT_OPTIONS, NETWORK_HEIGHT, DEFAULT_STYLESHEET
from functools import reduce


def scale_num(array, a, b):
    scaled = (b - a) * ((array - np.min(array)) / (np.max(array) - np.min(array))) + a
    return scaled.fillna(a)


def add_node_formatting(node_df,
                        label=None,
                        parent=None,
                        size_by=None,
                        min_size=20,
                        max_size=70,
                        opacity_by=None,
                        min_opacity=0.3,
                        max_opacity=0.8,
                        font_size_by=None,
                        font_min_size=20,
                        font_max_size=34,
                        ):
    if label:
        node_df['label'] = node_df[label]
    if parent:
        node_df.loc[:, 'parent'] = node_df[parent]
    if size_by:
        node_df['size'] = scale_num(node_df[size_by], min_size, max_size)
    if font_size_by:
        node_df['label_size'] = scale_num(node_df[size_by], font_min_size, font_max_size)

    if opacity_by:
        node_df['opacity'] = scale_num(node_df[opacity_by], min_opacity, max_opacity)

    return node_df


def format_cyto_nodes(node_df,
                      label=None,
                      classes='cyto_node',
                      **kwargs
                      ):
    node_df = add_node_formatting(node_df,
                                  label=label,
                                  **kwargs
                                  )
    nodes = node_df.rename(columns={label: 'id'}).to_dict('index')
    return [{'data': nodes[index], 'classes': classes} for index in nodes]


def format_cyto_edges(edge_df,
                      label=None,
                      classes='cyto_edge',
                      size_by=None,
                      min_size=4,
                      max_size=7,
                      opacity_by=None,
                      min_opacity=0.3,
                      max_opacity=0.6,
                      font_size_by=None,
                      font_min_size=12,
                      font_max_size=36,
                      ):
    if label:
        edge_df['label'] = edge_df[label]
    if size_by:
        edge_df['width'] = scale_num(edge_df['weight'], min_size, max_size)
    if font_size_by:
        edge_df['label_size'] = scale_num(edge_df['weight'], font_min_size, font_max_size)
    if opacity_by:
        edge_df['opacity'] = scale_num(edge_df['weight'], min_opacity, max_opacity)

    edges = edge_df.to_dict('index')
    return [{'data': edges[index], 'classes': classes} for index in edges]


def cyto_network(elements, is_dict=True):
    if is_dict:
        elements = list(reduce(lambda a, b: a + b, elements.values()))
    g = cyto.Cytoscape(
        id='cmu_net',
        layout=COSE_BILKENT_LAYOUT_OPTIONS,
        style={'width': '100%', 'height': NETWORK_HEIGHT},
        stylesheet=DEFAULT_STYLESHEET,
        elements=elements,
        autoRefreshLayout=False,
        # responsive=True,
    )

    return g
