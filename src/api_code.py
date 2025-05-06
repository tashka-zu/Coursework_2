from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Абстрактный базовый класс для парсеров вакансий
    """

    @abstractmethod
    def _connect_to_api(self):
        """Абстрактный метод для подключения к API"""
        pass

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
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        self.__file_worker = file_worker
        super().__init__()

    def _connect_to_api(self):
        """Подключение к API HeadHunter"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        return response.json()

    def load_vacancies(self, keyword):
        """Загружает вакансии с HeadHunter по заданному ключевому слову"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            data = self._connect_to_api()
            vacancies = data["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def vacancies(self):
        return self.__vacancies
