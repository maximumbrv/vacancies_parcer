import json
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self):
        pass

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
        self.file = None
        self.path = path

    def __enter__(self):
        self.open_file()
        return self.file

    def __exit__(self):
        self.file.close()
        self.file = None

    def open_file(self):
        self.file = open(self.path, 'a', encoding='utf-8')

    def close_file(self):
        if self.file is not None:
            self.file.close()

    def get_vacancies(self):
        pass

    def get_vacancies_by_keyword(self, keyword):
        pass

    def add_vacancies(self, *args):
        pass
