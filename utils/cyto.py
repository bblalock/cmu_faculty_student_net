import numpy as np

def scale_num(array, a, b):
    scaled = (b - a) * ((array - np.min(array)) / (np.max(array) - np.min(array))) + a
    if scaled is not None:
        return scaled
    else:
        return a


def format_cyto_nodes(node_df,
                      label='id',
                      classes='cyto_node',
                      parent=None,
                      size_by=None,
                      min_size=20,
                      max_size=70,
                      opacity_by=None,
                      min_opacity=0.3,
                      max_opacity=0.8,
                      ):
    if label:
        node_df['label'] = node_df[label]
    if parent:
        node_df.loc[:, 'parent'] = node_df[parent]
    if size_by:
        node_df['size'] = scale_num(node_df[size_by], min_size, max_size)
        node_df['label_size'] = scale_num(node_df[size_by], 16, 28)
    if opacity_by:
        node_df['opacity'] = scale_num(node_df[opacity_by], min_opacity, max_opacity)

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
                      ):
    if label:
        edge_df['label'] = edge_df[label]
    if size_by:
        edge_df['width'] = scale_num(edge_df['weight'], min_size, max_size)
    if opacity_by:
        edge_df['opacity'] = scale_num(edge_df['weight'], min_opacity, max_opacity)

    edges = edge_df.to_dict('index')
    return [{'data': edges[index], 'classes': classes} for index in edges]
