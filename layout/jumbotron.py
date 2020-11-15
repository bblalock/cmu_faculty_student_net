import dash_html_components as html
import dash_core_components as dcc


def get_children():
    children = html.Div(
        [
            dcc.Markdown(
                """
                ## Social Network Analysis of the Machine Learning Department at Carnegie Mellon University
                 
                This application was created in support of my application to CMU for Ph.D study in Machine Learning. The tools presented below allow for guided exploration of the patterns formed through collaboration among faculty and students during the dissertation process. 
                
                The motivations of this approach are to:
                
                1. focus on the content and culture of collaboration between faculty and students during the dissertation process as the most relevant and important factor when assessing institutions for doctoral study
                2. enable the user to form an impression of the department as a whole, without over indexing on any particular faculty while examining the opportunities the program has to offer  

                The data powering this application was scraped from the department’s [people pages](https://www.ml.cmu.edu/people/) and the [published dissertations of alumni](https://www.ml.cmu.edu/research/phd-dissertations.html). All code related to this project is availible on [github](https://github.com/bblalock/cmu_faculty_student_net).               
                """
            )
        ],
        id='jumbo_children'
    )
    return [children]


def initialize_jumbo_children():
    return get_children()
