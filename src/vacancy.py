class Vacancy:
    vacancies = []

    def __init__(self, name, url, salary, description, platform=None):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description
        self.platform = platform
        self.vacancies.append(self)

    def __repr__(self):
        representation = 'Vacancy(\n'
        representation += f'\tname = {self.name},\n'
        representation += f'\turl = {self.url},\n'
        representation += f'\tsalary = {self.salary},\n'
        representation += f'\tdescription = {self.description},\n'
        representation += f'\tplatform = {self.platform}\n)'
        return representation

    def __str__(self):
        return self.name

    @classmethod
    def instantiate_from_hh_list(cls, vacancies_list):
        for vacancy in vacancies_list:
            name = vacancy['name']
            url = vacancy['url']

            if vacancy['salary']:
                salary = {'from': vacancy['salary']['from'], 'to': vacancy['salary']['to']}
            else:
                salary = None

            snippet = vacancy['snippet']
            if snippet:
                if snippet['requirement'] is None:
                    del snippet['requirement']
                if snippet['responsibility'] is None:
                    del snippet['responsibility']
                description = '\n'.join(snippet.values())
            else:
                description = None

            platform = 'hh'

            cls.vacancies.append(cls(name, url, salary, description, platform))


