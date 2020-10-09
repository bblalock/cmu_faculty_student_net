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
        }
    },
    {
        'selector': '.faculty_root_node',
        'style': {'content': 'data(label)',
                  'font-size': '50px',
                  'compound-sizing-wrt-labels': 'include',
                  "border-color": "black",
                  "border-width": 2,
                  "border-opacity": 1,
                  'background-color': 'white',
                  "background-opacity": 0.0
                  }
    },
    {
        'selector': '.faculty_type_node',
        'style': {'content': 'data(label)',
                  'font-size': '30px',
                  'compound-sizing-wrt-labels': 'include',
                  "border-color": "black",
                  "border-width": 2,
                  "border-opacity": 1,
                  'background-color': 'grey',
                  "background-opacity": 0.2
                  }
    },
    {
        'selector': '.faculty_node',
        'style': {'content': 'data(label)',
                  'width': 'data(size)',
                  'height': 'data(size)',
                  'font-size': 'data(label_size)',
                  'background-opacity': 'data(opacity)',
                  'background-color': 'data(joint_community_color)',
                  "border-color": "data(joint_community_color)",
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
                  'line-color': "data(joint_community_color)",
                  'color': 'data(joint_community_color)',
                  'text-outline-color': "black",
                  'text-outline-opacity': 1,
                  'text-outline-width': 2,
                  'font-size': 'data(label_size)',
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
]

DEFAULT_STYLESHEET_DICT = {selector['selector']:selector for selector in DEFAULT_STYLESHEET }

COSE_BILKENT_LAYOUT_OPTIONS = {
    'name': 'cose-bilkent',
    'animationEasing': 'ease-out',
    ## 'draft', 'default' or 'proof"
    ## - 'draft' fast cooling rate
    ## - 'default' moderate cooling rate
    ## - "proof" slow cooling rate
    'quality': 'default',
    ## Whether to include labels in node dimensions. Useful for avoiding label overlap
    'nodeDimensionsIncludeLabels': 'true',
    ## number of ticks per frame; higher is faster but more jerky
    'refresh': 30,
    ## Whether to fit the network view after when done
    'fit': 'true',
    ## Padding on fit
    'padding': 0,
    ## Whether to enable incremental mode
    'randomize': 'true',
    ## Node repulsion (non overlapping) multiplier
    'nodeRepulsion': 4500,
    ## Ideal (intra-graph) edge length
    'idealEdgeLength': 0,
    ## Divisor to compute edge forces
    'edgeElasticity': 0.02,
    ## Nesting factor (multiplier) to compute ideal edge length for inter-graph edges
    'nestingFactor': 0.0,
    ## Maximum number of iterations to perform
    'numIter': 250,
    ## Whether to tile disconnected nodes
    'tile': 'true',
    ## Type of layout animation. The option set is {'during', 'end', false}
    'animate': 'end',
    ## Duration for animate:end
    'animationDuration': 500,
    ## Amount of vertical space to put between degree zero nodes during tiling (can also be a function)
    'tilingPaddingVertical': 0,
    ## Amount of horizontal space to put between degree zero nodes during tiling (can also be a function)
    'tilingPaddingHorizontal': 0,
    ## Gravity force (constant)
    'gravity': 0.5,
    ## Gravity range (constant) for compounds
    'gravityRangeCompound': 1.5,
    ## Gravity force (constant) for compounds
    'gravityCompound': 0.5,
    ## Gravity range (constant)
    'gravityRange': 3.8,
    ## Initial cooling factor for incremental layout
    'initialEnergyOnIncremental': 0.5
}
