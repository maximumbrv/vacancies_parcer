class Vacancy:
    vacancies = []

    def __init__(self, name, url, salary, description, platform=None):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description
        self.platform = platform
        self.vacancies.append(self)
