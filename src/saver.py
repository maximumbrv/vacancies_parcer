import json
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword):
        pass

    @abstractmethod
    def add_vacancies(self, *args):
        pass


class JSONSaver(Saver):

    def __init__(self, path='vacancies.json'):
        self.path = path

    def get_vacancies(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            file_raw = file.read()
        if file_raw:
            return json.loads(file_raw)
        else:
            return []

    def get_vacancies_by_keyword(self, keyword):
        pass

    def add_vacancies(self, *args):
        vacancies_from_file = self.get_vacancies()
        vacancies_from_file.extend(*args)
