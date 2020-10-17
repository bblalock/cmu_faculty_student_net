import dash_html_components as html
import dash_core_components as dcc

legend_children = [
    dcc.Markdown(
        """
    ##### Instructions / Legend:
    Clear instructions will go here
    Use these filters to highlight papers with:
    * bullet 1
    * bullet 2
    
    Try doing bla bla bla
    """
    ),
    html.Hr(className="my-2"),
]
