from dataclasses import dataclass
from typing import Optional, List
import json
from abc import ABC, abstractmethod


@dataclass
class Vacancy:
    title: str
    url: str
    salary: Optional[str]
    description: str

    def __post_init__(self):
        if not self.salary:
            self.salary = "Зарплата не указана"

    def __lt__(self, other):
        return self.salary < other.salary

class FileWorker(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self) -> List[dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

class JSONFileWorker(FileWorker):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def add_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies.append(vacancy)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> List[dict]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def delete_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v != vacancy]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
