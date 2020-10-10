import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

NETWORK_HEIGHT = '1100px'

DEFAULT_STYLESHEET = [
    {
        'selector': 'node',
        'style': {
            'text-transform': 'uppercase',
            'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
            'font-weight': 700,
            'color': 'white',
        }
    },
    {
        'selector': '.entity_root_node',
        'style': {'font-size': '50px',
                  'compound-sizing-wrt-labels': 'include',
                  "border-color": "white",
                  'background-color': 'white',
                  "background-opacity": 0.0
                  }
    },
    {
        'selector': '.entity_root_node.faculty',
        'style': {'content': 'data(label)',
                  "border-width": 2,
                  "border-opacity": 1,
                  }
    },
    {
        'selector': '.entity_root_node.student',
        'style': {'content': 'data(label)',
                  "border-width": 2,
                  "border-opacity": 1,
                  }
    },
    {
        'selector': '.entity_type_node',
        'style': {'content': 'data(label)',
                  'font-size': '30px',
                  'compound-sizing-wrt-labels': 'include',
                  "border-color": "white",
                  "border-width": 2,
                  "border-opacity": 1,
                  'background-color': 'grey',
                  "background-opacity": 0.2
                  }
    },
    {
        'selector': '.entity_node',
        'style': {'content': 'data(label)',
                  'width': 'data(size)',
                  'height': 'data(size)',
                  'font-size': 'data(label_size)',
                  'background-opacity': 'data(opacity)',
                  'background-color': 'data(community_color)',
                  "border-color": "data(community_color)",
                  "border-width": 2,
                  "border-opacity": 1,
                  'min-zoomed-font-size': '22px',
                  'display': 'data(display)'
                  }
    },
    {
        'selector': 'edge',
        'style': {'width': 'data(width)',
                  'opacity': 'data(opacity)',
                  'curve-style': 'bezier',
                  'text-transform': 'uppercase',
                  'font-family': 'News Cycle, Arial Narrow Bold, sans-serif',
                  'font-weight': 900,
                  'text-opacity': 1,
                  'line-color': "data(community_color)",
                  'color': 'data(community_color)',
                  'text-outline-color': "black",
                  'text-outline-opacity': 1,
                  'text-outline-width': 2,
                  'font-size': '24px',
                  'text-rotation': 'autorotate',
                  'label': 'data(relationship)',
                  'min-zoomed-font-size': '36px'
                  }
    },
    {
        'selector': '.co_advised_edge',
        'style': {'line-style': 'solid'}
    },
    {
        'selector': '.co_committee_edge',
        'style': {'line-style': 'dashed'}
    },
    {
        'selector': '.advised_edge',
        'style': {'line-style': 'solid',
                  'width': 3,
                  'opacity': 0.2,
                  'line-color': "#A9A9A9",
                  'color': 'white',
                  'text-outline-color': "black",
                  'text-outline-opacity': 1,
                  'text-outline-width': 1,
                  'min-zoomed-font-size': '30px',
                  'target-arrow-shape': 'triangle',
                  'target-arrow-color': 'white',
                  'target-arrow-fill': 'filled',
                  'arrow-scale': 3,
                  }
    },

]

DEFAULT_STYLESHEET_DICT = {selector['selector']: selector for selector in DEFAULT_STYLESHEET}

COSE_BILKENT_LAYOUT_OPTIONS = {
    'name': 'cose-bilkent',
    'animationEasing': 'ease-out',
    ## 'draft', 'default' or 'proof"
    ## - 'draft' fast cooling rate
    ## - 'default' moderate cooling rate
    ## - "proof" slow cooling rate
    'quality': 'draft',
    ## Whether to include labels in node dimensions. Useful for avoiding label overlap
    'nodeDimensionsIncludeLabels': 'true',
    ## number of ticks per frame; higher is faster but more jerky
    'refresh': 30,
    ## Whether to fit the network view after when done
    'fit': 'true',
    ## Padding on fit
    'padding': 3,
    ## Whether to enable incremental mode
    'randomize': 'true',
    ## Node repulsion (non overlapping) multiplier
    'nodeRepulsion': 45,
    ## Ideal (intra-graph) edge length
    'idealEdgeLength': 0,
    ## Divisor to compute edge forces
    'edgeElasticity': 0.02,
    ## Nesting factor (multiplier) to compute ideal edge length for inter-graph edges
    'nestingFactor': 0.0,
    ## Maximum number of iterations to perform
    'numIter': 250,
    ## Whether to tile disconnected nodes
    'tile': 'False',
    ## Type of layout animation. The option set is {'during', 'end', false}
    'animate': 'false',
    ## Duration for animate:end
    'animationDuration': 500,
    ## Amount of vertical space to put between degree zero nodes during tiling (can also be a function)
    'tilingPaddingVertical': 0,
    ## Amount of horizontal space to put between degree zero nodes during tiling (can also be a function)
    'tilingPaddingHorizontal': 0,
    ## Gravity force (constant)
    'gravity': 0.5,
    ## Gravity range (constant)
    'gravityRange': 3.8,
    ## Gravity force (constant) for compounds
    'gravityCompound': 10.0,
    ## Gravity range (constant) for compounds
    'gravityRangeCompound': 0.9,
    ## Initial cooling factor for incremental layout
    'initialEnergyOnIncremental': 0.5
}
