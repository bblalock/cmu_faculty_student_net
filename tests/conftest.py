from constants import ROOT_DIR
import pandas as pd
import pytest


@pytest.fixture(scope="session")
def test_phd_student_df():
    df = pd.read_csv(ROOT_DIR + '/data/test/current_phd_students.csv').fillna('')
    return df


@pytest.fixture(scope="session")
def test_core_faculty_df():
    df = pd.read_csv(ROOT_DIR + '/data/test/core_faculty.csv').fillna('')
    return df


@pytest.fixture(scope="session")
def test_affiliated_faculty_df():
    df = pd.read_csv(ROOT_DIR + '/data/test/affiliated_faculty.csv').fillna('')
    return df


@pytest.fixture(scope="session")
def test_related_faculty_df():
    df = pd.read_csv(ROOT_DIR + '/data/test/related_faculty.csv').fillna('')
    return df


@pytest.fixture(scope="session")
def test_alumni_people_df():
    df = pd.read_csv(ROOT_DIR + '/data/test/alumni_phd.csv').fillna('')
    return df
