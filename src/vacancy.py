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

    def __lt__(self, other):


    @classmethod
    def instantiate_from_hh_list(cls, vacancies_list):
        for vacancy in vacancies_list:
            name = vacancy['name']
            url = vacancy['url']

            salary = {'from': None, 'to': None}
            if vacancy['salary'] is not None:
                if vacancy['salary']['to'] is not None:
                    salary['to'] = vacancy['salary']['to']
                if vacancy['salary']['from'] is not None:
                    salary['from'] = vacancy['salary']['from']
            if salary['from'] is None and salary['to'] is None:
                salary = None

            snippet = vacancy['snippet']
            if snippet is not None:
                if snippet['requirement'] is None:
                    del snippet['requirement']
                else:
                    snippet['requirement'] = snippet['requirement'].replace('<highlighttext>', '')
                    snippet['requirement'] = snippet['requirement'].replace('</highlighttext>', '')
                if snippet['responsibility'] is None:
                    del snippet['responsibility']
                else:
                    snippet['responsibility'] = snippet['responsibility'].replace('<highlighttext>', '')
                    snippet['responsibility'] = snippet['responsibility'].replace('</highlighttext>', '')
                description = '\n'.join(snippet.values())
            else:
                description = None

            platform = 'HeadHunter'

            cls.vacancies.append(cls(name, url, salary, description, platform))

    @classmethod
    def instantiate_from_sj_list(cls, vacancies_list):
        for vacancy in vacancies_list:
            name = vacancy['profession']
            url = vacancy['link']

            salary = {'from': None, 'to': None}
            if vacancy['payment_from']:
                salary['from'] = vacancy['payment_from']
            if vacancy['payment_to']:
                salary['to'] = vacancy['payment_to']
            if salary['from'] is None and salary['to'] is None:
                salary = None

            if vacancy['candidat']:
                description = vacancy['candidat']
            else:
                description = None

            platform = 'SuperJob'

            cls.vacancies.append(cls(name, url, salary, description, platform))
