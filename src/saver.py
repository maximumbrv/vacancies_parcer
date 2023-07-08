import json
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def close_file(self):
        pass

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
        self.file = self.open_file()

    def open_file(self):
        return open(self.path, 'a+', encoding='utf-8')

    def close_file(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def get_vacancies(self):
        file_raw = self.file.read()
        if file_raw:
            return json.loads(file_raw).decode()
        else:
            return []

    def get_vacancies_by_keyword(self, keyword):
        pass

    def add_vacancies(self, *args):
        vacancies_from_file = self.get_vacancies()
        vacancies_from_file.append(args)
        json.dump(vacancies_from_file, self.file)
