import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

NETWORK_HEIGHT = '1100px'

FILTERABLE_EDGE_CLASSES = ['co_advised_edge faculty',
                           'co_committee_edge faculty',
                           'co_advised_edge student',
                           # 'co_committee_edge student'
                           ]

DEFAULT_STYLESHEET = [
    {
        'selector': 'node',
        'style': {
            'color': 'white',
            'text-transform': 'uppercase',
            'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
            'font-weight': 700,
            "border-width": 2,
            "border-opacity": 1,
            'content': 'data(label)',
            'display': 'element'
        }
    },
    {
        'selector': '.entity_root_node',
        'style': {'compound-sizing-wrt-labels': 'include',
                  'font-size': '50px',
                  "border-color": "white",
                  'background-color': 'white',
                  "background-opacity": 0.0,
                  }
    },
    {
        'selector': '.entity_type_node',
        'style': {'compound-sizing-wrt-labels': 'include',
                  'font-size': '30px',
                  "border-color": "white",
                  'background-color': 'white',
                  "background-opacity": 0.2,
                  }
    },
    {
        'selector': '.entity_node',
        'style': {'width': 'data(size)',
                  'height': 'data(size)',
                  'font-size': 'data(label_size)',
                  'background-opacity': 'data(opacity)',
                  'background-color': 'data(community_color)',
                  "border-color": "data(community_color)",
                  }
    },
    {
        'selector': '.entity_node.faculty',
        'style': {'min-zoomed-font-size': '18px'}
    },
    {
        'selector': '.entity_node.student',
        'style': {'min-zoomed-font-size': '32px'}
    },
    {
        'selector': 'edge',
        'style': {'label': 'data(relationship)',
                  'width': 'data(width)',
                  'curve-style': 'bezier',
                  'text-transform': 'uppercase',
                  'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                  'font-weight': 900,
                  'text-opacity': 1,
                  # 'opacity': 'data(opacity)',
                  'line-color': "data(community_color)",
                  'color': 'white',
                  'font-size': 22,
                  'text-outline-color': 'black',
                  'text-outline-opacity': 1,
                  'text-outline-width': 5,
                  'text-rotation': 'autorotate',
                  }
    },
    {
        'selector': '.co_advised_edge',
        'style': {'line-style': 'solid',
                  'opacity': 0.5,
                  'min-zoomed-font-size': '40px'
                  }
    },
    {
        'selector': '.co_committee_edge',
        'style': {'line-style': 'dashed',
                  'opacity': 0.3,
                  'min-zoomed-font-size': '50px'
                  }
    },
    {
        'selector': '.bipartite_advised_edge',
        'style': {'line-style': 'solid',
                  'width': 3,
                  'opacity': 0.2,
                  'source-arrow-shape': 'tee',
                  'source-arrow-color': 'data(community_color)',
                  'source-arrow-fill': 'filled',
                  'target-arrow-shape': 'triangle',
                  'target-arrow-color': 'data(community_color)',
                  'target-arrow-fill': 'filled',
                  'arrow-scale': 5,
                  'min-zoomed-font-size': '40px'
                  }
    },
    {
        "selector": '.entity_node[degree = 0]',
        "style": {
            'content': '',
            'font-size': 0,
        }
    }
]

DEFAULT_STYLESHEET_DICT = {selector['selector']: selector for selector in DEFAULT_STYLESHEET}

COSE_BILKENT_LAYOUT_OPTIONS = {
    'name': 'cose-bilkent',
    # 'animationEasing': 'ease-out',
    # 'zoom': 0,
    ## 'draft', 'default' or 'proof"
    ## - 'draft' fast cooling rate
    ## - 'default' moderate cooling rate
    ## - "proof" slow cooling rate
    'quality': 'proof',
    ## Whether to include labels in node dimensions. Useful for avoiding label overlap
    'nodeDimensionsIncludeLabels': True,
    ## number of ticks per frame; higher is faster but more jerky
    'refresh': 200,
    ## Whether to fit the network view after when done
    'fit': True,
    ## Padding on fit
    'padding': 1,
    ## Whether to enable incremental mode
    'randomize': True,
    ## Node repulsion (non overlapping) multiplier
    'nodeRepulsion': 50000,
    # ## Ideal (intra-graph) edge length
    'idealEdgeLength': 200,
    # Divisor to compute edge forces
    'edgeElasticity': 0.3,
    # ## Nesting factor (multiplier) to compute ideal edge length for inter-graph edges
    # 'nestingFactor': 0.01,
    # ## Maximum number of iterations to perform
    # 'numIter': 200,
    ## Whether to tile disconnected nodes
    'tile': True,
    ## Type of layout animation. The option set is {'during', 'end', false}
    'animate': 'during',
    # ## Duration for animate:end
    'animationDuration': 100,
    ## Amount of vertical space to put between degree zero nodes during tiling (can also be a function)
    'tilingPaddingVertical': 0,
    ## Amount of horizontal space to put between degree zero nodes during tiling (can also be a function)
    'tilingPaddingHorizontal': 0,
    # ## Gravity force (constant)
    'gravity': 0.5,
    # ## Gravity range (constant)
    'gravityRange': 2.5,
    # # Gravity force (constant) for compounds
    'gravityCompound': 5.0,
    # ## Gravity range (constant) for compounds
    'gravityRangeCompound': 0.7,
    # ## Initial cooling factor for incremental layout
    'initialEnergyOnIncremental': 0.5
}
