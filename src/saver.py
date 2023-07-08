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
        self.file = self.open_file()
        self.open_file()

    def open_file(self):
        return open(self.path, 'w', encoding='utf-8')

    def close_file(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def get_vacancies(self):
        pass

    def get_vacancies_by_keyword(self, keyword):
        pass

    def add_vacancies(self, *args):
        json_raw = json.dumps(args)
        self.file.write(json_raw)
