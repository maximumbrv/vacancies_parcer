from src.api import HeadHunterAPI, SuperJobApi
from src.vacancy import Vacancy


def user_interaction():
    hh = HeadHunterAPI()
    hh.get_vacancies('Python')
    sj = SuperJobApi()
    sj.get_vacancies('Python')
    Vacancy.instantiate_from_sj_list(sj.vacancies)
    for vac in Vacancy.vacancies:
        print(repr(vac))
        print()



if __name__ == '__main__':
    user_interaction()
