import pandas as pd
import networkx as nx
import plotly.express as px


def cooccurrence_edgelist(df, on):
    entity = 'faculty' if 'student' in on else 'student'
    edgelist = pd.merge(df, df, on=on, how='inner')
    edgelist = edgelist[edgelist[entity + '_x'] != edgelist[entity + '_y']]
    edgelist['pair'] = edgelist[[entity + '_x', entity + '_y']].values.tolist()
    edgelist['pair'] = edgelist['pair'].apply(lambda x: sorted(x))
    edgelist[['source', 'target']] = pd.DataFrame(edgelist.pair.tolist(), index=edgelist.index)
    edgelist['relationship'] = edgelist.apply(
        lambda x: 'Co-Advised' if (x['edge_type_x'] == 'Advisor') and (x.edge_type_y == 'Advisor') else 'Co-Committee',
        axis=1)
    edgelist = edgelist.groupby(['source', 'target', 'relationship']).size().reset_index(name='weight')
    return edgelist

color_scale = px.colors.qualitative.Light24

def get_color(i, n=len(color_scale)):
    return color_scale[i - 1] if i < n else 'rgb(1,1,1)'


def get_nx_graph(edge_file, node_file, create_using=nx.DiGraph):
    g = nx.from_pandas_edgelist(
        edge_file,
        'source',
        'target',
        edge_attr=['weight', 'relationship'],
        create_using=create_using
    )

    # print('')
    # print([edge for edge in g.edges if 'Manuela Veloso' in edge])

    node_attr = node_file.set_index('id').to_dict('index')
    nx.set_node_attributes(g, node_attr)
    return g


def set_node_degree(G, name='degree'):
    degree = G.degree
    for v in G:
        G.nodes[v][name] = degree[v]


def set_node_pagerank(G, name='pagerank', **kwargs):
    pr = nx.pagerank(G, **kwargs)
    for v in G:
        G.nodes[v][name] = pr[v]


def set_node_community(G, name='community'):
    # communities = sorted(nx.community.greedy_modularity_communities(G), key=len, reverse=True)
    # communities = sorted(next(nx.community.girvan_newman(G)), key=len, reverse=True)
    communities = nx.community.label_propagation_communities(G.to_undirected())
    # communities = nx.community.asyn_lpa_communities(G, weight='weight')
    communities = sorted(communities, key=len, reverse=True)

    # degrees = nx.get_node_attributes(G, 'degree')
    # degrees = G.degree
    '''Add community to node attributes'''
    i = 0
    for v_c in communities:
        valid_community = False
        if len(v_c) > 2:
            valid_community = True
            for v in v_c:
                # Add 1 to save 0 for external edges
                G.nodes[v][name] = i + 1
                G.nodes[v][name + '_color'] = get_color(i, min(len(communities), len(color_scale)))
        else:
            for v in v_c:
                G.nodes[v][name] = 0
                G.nodes[v][name + '_color'] = 'rgb(1,1,1)'
        if valid_community:
            i = i + 1


def set_edge_community(G, name='community'):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
        if G.nodes[v][name] == G.nodes[w][name]:
            # Internal edge, mark with community
            G.edges[v, w][name] = G.nodes[v][name]
            G.edges[v, w][name + '_color'] = G.nodes[v][name + '_color']
        else:
            # External edge, mark as 0
            G.edges[v, w][name] = 0
            G.edges[v, w][name + '_color'] = 'grey'


def add_zero_degree_nodes(g, node_df, name_prefix):
    node_attr = node_df.set_index('id').to_dict('index')
    for node in node_attr:
        if node not in g:
            g.add_node(node)
            attr = node_attr[node]
            attr[name_prefix + 'degree'] = 0
            attr[name_prefix + 'pagerank'] = 0
            attr[name_prefix + 'community'] = 0
            attr[name_prefix + 'community_color'] = 'rgb(1,1,1)'
            nx.set_node_attributes(g, {node: attr})

    return g


def create_node_edge_frame(G):
    node_attr = {node: G.nodes[node] for node in G.nodes}
    edge_attr = {edge: G.edges[edge[0], edge[1]] for edge in G.edges}


    node_frame = pd.DataFrame.from_dict(node_attr, orient='index').rename_axis('id').reset_index()
    edge_frame = pd.DataFrame.from_dict(edge_attr, orient='index').rename_axis(['source', 'target']).reset_index()

    return node_frame, edge_frame


def get_node_edge_frame(node_df, edgelist_df, name_prefix=''):
    G = get_nx_graph(edgelist_df, node_df, create_using=nx.DiGraph)

    # Set node and edge communities
    set_node_degree(G, name=name_prefix + 'degree')
    set_node_pagerank(G, name=name_prefix + 'pagerank')
    set_node_community(G, name=name_prefix + 'community')
    set_edge_community(G, name=name_prefix + 'community')

    G = add_zero_degree_nodes(G, node_df, name_prefix)

    # print(G.edges('Manuela Veloso'))

    # print(edgelist_df[edgelist_df['source'] == 'Manuela Veloso'])
    # Create node and edge_frame
    node_frame, edge_frame = create_node_edge_frame(G)
    node_frame['display'] = 'element'

    # print(edge_frame[edge_frame['source'] == 'Manuela Veloso'])

    return node_frame, edge_frame
