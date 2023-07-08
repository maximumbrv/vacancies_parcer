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
        try:
            file = open(self.path, 'r', encoding='utf-8')
            file_raw = file.read()
            file.close()
            return json.loads(file_raw)
        except FileNotFoundError:
            return []

    def get_vacancies_by_keyword(self, keyword):
        vacancies_from_file = self.get_vacancies()
        filtered_vacancies = []
        for vacancy in vacancies_from_file:
            if keyword in vacancy['name'] or keyword in vacancy['description']:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def add_vacancies(self, *args):
        vacancies_from_file = self.get_vacancies()
        vacancies_from_file.extend(*args)
        with open(self.path, 'w', encoding='utf-8') as file:
            file.truncate(0)
            json.dump(vacancies_from_file, file)

