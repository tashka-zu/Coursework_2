import json
import os

from src.classes_vacancy import JSONFileWorker, Vacancy


def test_vacancy_initialization():
    """Тест для проверки инициализации объекта вакансии"""
    vacancy = Vacancy(
        title="Test Vacancy", url="http://test.url", salary="50000-60000", description="Test description"
    )
    assert vacancy.title == "Test Vacancy"
    assert vacancy.url == "http://test.url"
    assert vacancy.salary == "50000-60000"
    assert vacancy.description == "Test description"


def test_json_file_worker():
    """Тест для проверки работы с JSON-файлами через класс JSONFileWorker"""
    filename = "test_vacancies.json"
    if os.path.exists(filename):
        os.remove(filename)

    file_worker = JSONFileWorker(filename=filename)
    vacancy = Vacancy(
        title="Test Vacancy", url="http://test.url", salary="50000-60000", description="Test description"
    )
    file_worker.add_vacancy(vacancy)  # Передаем объект Vacancy, а не словарь

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["title"] == "Test Vacancy"

    os.remove(filename)
