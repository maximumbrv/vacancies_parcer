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
