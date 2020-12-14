# CMU MLD Faculty, Student, and Alumni Web Scraping and Network Analysis

## Hosted App 
The application is currently hosted live at https://cmu-faculty-student-net.herokuapp.com/

## What is it
This code base contains both a webscraping pipeline and a Plotly Dash application used in 
creation of the above application. 

### Webscraper
This application is powered with data scraped from the [people pages](https://www.ml.cmu.edu/people/) of the 
department's website as well as the published [PhD dissertations](https://www.ml.cmu.edu/research/phd-dissertations.html) 
and [technical reports](https://www.ml.cmu.edu/research/technical-reports.html) of the programs alumni -- 
both in pdf format.

All code relevant to this pipeline is in `cmu_faculty_student_net/web_scraper` and `cmu_faculty_student_net/scripts`.
Output is written to `cmu_faculty_student_net/data`

The scripts which generate the underlying data powering the application are ran in the following order:
1. scrape_cmu.py
2. transform_faculty_current_students.py
3. transform_alumni.py
4. create_match_review_frame.py (this script produces an output which is then manually QA'd)
5. create_node_edge_files.py

For explanatory purposes, this repo included the final data used to power the final application in `data/app/`

### Plotly Dash Web Application
Most of the code relevant to the front-end portion of this project is in `cmu_faculty_student_net/utils`, 
`cmu_faculty_student_net/callbacks`, and `cmu_faculty_student_net/layout`.

To run the application execute `python app.py` from the command line. The application is currently hosted at 
https://cmu-faculty-student-net.herokuapp.com/.



