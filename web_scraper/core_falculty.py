from functools import reduce
from web_scraper import CmuScraper


class CoreFacultyScraper(CmuScraper):
    def __init__(self, test=False):
        super().__init__(test=test)
        self.label = 'core_faculty'
        self.url = self.route_root + 'core-faculty.html'

    def scrape_site(self):
        if self.soup is None:
            self._get_html_soup()

        core_fac_grid = self.soup.find("div", attrs={"id": "faculty-cards"})
        mld_core_fac = core_fac_grid.find_all("div")

        core_faculty_data = []
        for faculty in mld_core_fac:
            name = faculty.find('h2')
            if name:
                faculty_row = {'entity_type': 'faculty', 'entity_subtype': 'core', 'name': name.text.strip()}

                title = faculty.find('h3')
                faculty_row['title'] = title.text.strip()

                research_interests = faculty.find('ul', attrs={'class': 'keywords-ib'})
                if research_interests:
                    research_interests = research_interests.find_all('li')
                    research_interests = reduce(lambda s1, s2: s1 + ', ' + s2,
                                                [t.text.strip() for t in research_interests]
                                                )
                    faculty_row['research_interests'] = research_interests
                    faculty_row['research_interests'] = research_interests#.split(",")

                core_faculty_data.append(faculty_row)
        self.scraped_data = core_faculty_data

    def get_output_dataframe(self):
        super().get_output_dataframe()
        return self.output_dataframe
