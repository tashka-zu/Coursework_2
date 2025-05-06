from dataclasses import dataclass, asdict
from typing import Optional, List
import json
from abc import ABC, abstractmethod

@dataclass
class Vacancy:
    """
    Класс для представления вакансии
    """
    title: str
    url: str
    salary: Optional[str]
    description: str

    def to_dict(self):
        """Преобразует объект Vacancy в словарь"""
        return asdict(self)

    def __post_init__(self):
        """Инициализация после создания объекта"""
        if not self.salary:
            self.salary = "Зарплата не указана"

    def __lt__(self, other):
        """Сравнивает вакансии по зарплате"""
        return self.salary < other.salary

class FileWorker(ABC):
    """
    Абстрактный базовый класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self) -> List[dict]:
        """Получает список вакансий из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из файла"""
        pass


class JSONFileWorker(FileWorker):
    """
    Класс для работы с JSON-файлами
    """
    def __init__(self, filename='vacancies.json'):
        """Инициализация класса JSONFileWorker"""
        self.filename = filename

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в JSON-файл"""
        vacancies = self.get_vacancies()
        vacancies.append(vacancy)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> List[dict]:
        """Получает список вакансий из JSON-файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из JSON-файла"""
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v != vacancy]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)