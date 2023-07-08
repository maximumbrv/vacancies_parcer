class Vacancy:
    vacancies = []
    ids = set()

    def __init__(self, id, name, url, salary, description, platform=None):
        if id in Vacancy.ids:
            raise Exception('vacancy already in the list')
        self.id = id
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

    def are_comparable(self, other):
        return self.salary['from'] is not None and other.salary['from'] is not None

    def __lt__(self, other):
        if self.are_comparable(other):
            return self.salary['from'] < other.salary['from']
        else:
            raise ValueError('items not comparable')

    def __gt__(self, other):
        if self.are_comparable(other):
            return self.salary['from'] > other.salary['from']
        else:
            raise ValueError('items not comparable')

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        if self.are_comparable(other):
            return self.salary['from'] == other.salary['from']
        else:
            raise ValueError('items not comparable')

    def __neq__(self, other):
        return not self.__eq__(other)

    @classmethod
    def instantiate_from_hh_list(cls, vacancies_list):
        for vacancy in vacancies_list:
            id = 'hh' + vacancy['id']
            if id in cls.ids:
                return None
            name = vacancy['name']
            url = vacancy['url']

            salary = {'from': None, 'to': None}
            if vacancy['salary'] is not None:
                if vacancy['salary']['to'] is not None:
                    salary['to'] = vacancy['salary']['to']
                if vacancy['salary']['from'] is not None:
                    salary['from'] = vacancy['salary']['from']

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

            cls.vacancies.append(cls(id, name, url, salary, description, platform))

    @classmethod
    def instantiate_from_sj_list(cls, vacancies_list):
        for vacancy in vacancies_list:
            id = 'sj' + vacancy['id']
            if id in cls.ids:
                return None
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

            cls.vacancies.append(cls(id, name, url, salary, description, platform))
