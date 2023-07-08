import pytest
from src.api import HeadHunterAPI, SuperJobApi


def test_hh_get_vacancies():
    hh = HeadHunterAPI()
    hh.get_vacancies('Python')
    assert len(hh.vacancies) > 0

def test_sj_get_vacancies():
    sj = SuperJobApi()
    sj.get_vacancies('Python')
    assert len(sj.vacancies) > 0