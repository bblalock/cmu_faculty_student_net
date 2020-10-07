import pandas as pd
from web_scraper.phd_students import PhdStudentScraper
from web_scraper.affiliated_falculty import AffiliatedFacultyScraper
from web_scraper.core_falculty import CoreFacultyScraper
from web_scraper.related_faculty import RelatedFacultyScraper
from web_scraper.alumni import AlumniPeoplePageScraper
from web_scraper.alumni import AlumniPdfThesisScraper
from web_scraper.alumni import AlumniAbstractScraper

if __name__ == "__main__":
    core_faculty = CoreFacultyScraper()
    core_faculty.write_to_csv()

    affiliated_faculty = AffiliatedFacultyScraper()
    affiliated_faculty.write_to_csv()

    related_faculty = RelatedFacultyScraper()
    related_faculty.write_to_csv()

    phd_students = PhdStudentScraper()
    phd_students.write_to_csv()

    alumni = AlumniPeoplePageScraper()
    alumni.write_to_csv()

    alumni_master = alumni.get_output_dataframe()

    faculty_master = pd.concat(map(lambda x: x.get_output_dataframe(),
                                   [core_faculty, affiliated_faculty, related_faculty]
                                   )
                               )

    dissertation_pdf_scrape = AlumniPdfThesisScraper(alumni_master, faculty_master)
    dissertation_pdf_scrape.write_to_csv()

    dissertation_abstract_scrape = AlumniAbstractScraper(alumni_master, faculty_master)
    dissertation_abstract_scrape.write_to_csv()

