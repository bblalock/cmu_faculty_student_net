from web_scraper.phd_students import PhdStudentScraper
from web_scraper.affiliated_falculty import AffiliatedFacultyScraper
from web_scraper.core_falculty import CoreFacultyScraper
from web_scraper.related_faculty import RelatedFacultyScraper
from web_scraper.alumni import AlumniPeoplePageScraper

from pandas._testing import assert_frame_equal


def test_phd_student(test_phd_student_df):
    phd_students = PhdStudentScraper(test=True).get_output_dataframe().fillna('')
    assert_frame_equal(phd_students, test_phd_student_df)


def test_core_faculty(test_core_faculty_df):
    core_faculty = CoreFacultyScraper(test=True).get_output_dataframe().fillna('')
    assert_frame_equal(core_faculty, test_core_faculty_df)


def test_affiliated_faculty(test_affiliated_faculty_df):
    affiliated_faculty = AffiliatedFacultyScraper(test=True).get_output_dataframe().fillna('')
    assert_frame_equal(affiliated_faculty, test_affiliated_faculty_df)


def test_related_faculty(test_related_faculty_df):
    related_faculty = RelatedFacultyScraper(test=True).get_output_dataframe().fillna('')
    assert_frame_equal(related_faculty, test_related_faculty_df)

def test_alumni(test_alumni_people_df):
    alumni = AlumniPeoplePageScraper(test=True).get_output_dataframe().fillna('')
    assert_frame_equal(alumni, test_alumni_people_df)
