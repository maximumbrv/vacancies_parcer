import requests
import json
from abc import ABC, abstractmethod
from api_key import SUPERJOB_KEY


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
        self.key = SUPERJOB_KEY
        self.vacancies = []

    def get_vacancies(self, keyword):
        headers = {'X-Api-App-Id': self.key}
        params = {'keyword': keyword}
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', params=params, headers=headers)
        self.vacancies = response.json()['objects']

    def to_list(self):
        return self.vacancies


