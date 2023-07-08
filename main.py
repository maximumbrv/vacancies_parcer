from src.api import HeadHunterAPI
from src.vacancy import Vacancy


def user_interaction():
    hh = HeadHunterAPI()
    hh.get_vacancies('Python')
    print(hh.to_list()[0])


if __name__ == '__main__':
    user_interaction()
