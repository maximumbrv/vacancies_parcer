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
    def open(self):
        pass

    @abstractmethod
    def close(self):
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
        pass

    def get_vacancies(self):
        pass

    def get_vacancies_by_keyword(self, keyword):
        pass

    def add_vacancies(self, *args):
        pass
