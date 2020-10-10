from functools import reduce
from web_scraper import CmuScraper
import re


class PhdStudentScraper(CmuScraper):
    def __init__(self, test=False):
        super().__init__(test=test)
        self.label = 'current_phd_students'
        self.url = self.route_root + 'phd-students.html'

    def scrape_site(self):
        if self.soup is None:
            self._get_html_soup()

        phd_grid = self.soup.find("div", attrs={"id": "people-bios-grid-card"})
        phd_students = phd_grid.find_all("div")

        student_data = []
        for student in phd_students:
            header = student.find('h2')
            if header:
                student_row = {'name': header.text}

                body = student.find_all('p')
                body = reduce(lambda s1, s2: s1 + ', ' + s2,
                              list(map(lambda p: p.get_text(separator=', ', strip=True), body))
                              )

                if body.index(", Advisor") < body.index(", Research "):
                    body = re.split(', Advisor:|, Advisors:', body)
                    student_row['education'] = body[0].strip()

                    body = re.split(', Research Interests:|, Research interests:|, Research Interest:', body[1])
                    advisor = body[0].strip()
                    research_interests = body[1].strip()

                else:
                    body = re.split(', Research Interests:|, Research interests:|, Research Interest:', body)
                    student_row['education'] = body[0].strip()

                    body = re.split(', Advisor:|, Advisors:', body[1])
                    advisor = body[1].strip()
                    research_interests = body[0].strip()

                student['entity_type'] = 'student'
                student_row['entity_subtype'] = 'current_student'
                student_row['advisor'] = advisor.replace(' & ', ' , ')
                student_row['advisor'] = student_row['advisor']#.split(",")
                student_row['research_interests'] = research_interests#.split(",")

                student_data.append(student_row)
        self.scraped_data = student_data

    def get_output_dataframe(self):
        super().get_output_dataframe()
        return self.output_dataframe
