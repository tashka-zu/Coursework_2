import requests
from abc import ABC, abstractmethod

class Parser(ABC):
    """
    Абстрактный базовый класс для парсеров вакансий
    """
    @abstractmethod
    def load_vacancies(self, keyword):
        """Абстрактный метод для загрузки вакансий"""
        pass

class HH(Parser):
    """
    Класс для работы с API HeadHounter
    """

    def __init__(self, file_worker):
        """Инициализация класса HH"""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__()

    def load_vacancies(self, keyword):
        """Загружает вакансии с HeadHunter по заданному ключевому слову"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
