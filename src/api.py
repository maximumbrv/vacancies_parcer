import requests
import json
from abc import ABC, abstractmethod


class API(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def to_list(self):
        pass


class HeadHunterAPI(API):
    def __init__(self):
        self.vacancies = []

    def get_vacancies(self, keyword=''):
        params = {'area': 113, 'text': keyword, 'per_page': 20}
        response = requests.get('https://api.hh.ru/vacancies', params)
        print(response.status_code)
        vacancies_list = response.json()['items']
        self.vacancies = vacancies_list

    def to_list(self):
        return self.vacancies


class SuperJobApi(API):

    def __init__(self):
        pass

    def get_vacancies(self, keyword):
        pass

    def to_list(self):
        pass

