import dash_html_components as html
import dash_core_components as dcc

legend_children = [
    dcc.Markdown(
        """
    ##### Instructions:
    The network below shows a compound graph representation of faculty advising relationships form among the dissertation committees of the [ML Department at Carnegie Mellon University](https://www.ml.cmu.edu/).
    
    Three different types of edges are present in the above network: 
    
    * **Co-Advisor edges**, denoted as solid lines, are drawn between faculty or students who respectively advised the same student or were advised by the same faculty member
    * **Co-Committee edges** are dashed-lines drawn between faculty who serve on the same dissertation committee
    * **Advisor edges** are solid lines with arrows drawn from faculty members connecting to the students they’ve advised. 
    
    A modified [label propagation algorithm](https://arxiv.org/abs/0709.2938) was use to identify naturally occurring research communities from these relationships.  The algorithm was modified to account for the multi-graph nature of these relationships; edge-weights for Co-Committee edges were dampedned by a factor of five and Advisor edge-weights were amplified by a factor of three to ensure faculty almost always have the same community membership as the students they advised.  Color denotes community membership, with intra-community edges saturated with their community’s respective color and inter-community edges colored grey.
    
    Use the controls below to filter the relationships presented in the visual. In addition to these controls, the user can **click on individual nodes** to highlight all of their connections and **zoom in and out** of the visualization to reveal the labels of nodes and edges. 
    """
    ),
    html.Hr(className="my-2"),
]
