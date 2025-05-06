from src.classes_vacancy import Vacancy
from src.utils import (
    convert_to_vacancy_objects,
    filter_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    get_top_vacancies,
    print_vacancies
)

def test_filter_vacancies():
    """Тест для функции фильтрации вакансий по ключевым словам в описании"""
    vacancies = [
        Vacancy(title="Vacancy 1", url="http://url1.com", salary="50000", description="Description with work"),
        Vacancy(title="Vacancy 2", url="http://url2.com", salary="60000", description="Description without job")
    ]
    filtered = filter_vacancies(vacancies, ["work"])
    assert len(filtered) == 1
    assert filtered[0].title == "Vacancy 1"


def test_get_vacancies_by_salary():
    """Тест для функции фильтрации вакансий по зарплате"""
    vacancies = [
        Vacancy(title="Vacancy 1", url="http://url1.com", salary="50000", description="Description 1"),
        Vacancy(title="Vacancy 2", url="http://url2.com", salary="60000", description="Description 2")
    ]
    filtered = get_vacancies_by_salary(vacancies, "55000-65000")
    assert len(filtered) == 1
    assert filtered[0].title == "Vacancy 2"


def test_sort_vacancies():
    """Тест для функции сортировки вакансий по зарплате"""
    vacancies = [
        Vacancy(title="Vacancy 1", url="http://url1.com", salary="50000", description="Description 1"),
        Vacancy(title="Vacancy 2", url="http://url2.com", salary="60000", description="Description 2")
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0].title == "Vacancy 2"


def test_convert_to_vacancy_objects():
    vacancies_data = [
        {
            'name': 'Vacancy 1',
            'alternate_url': 'http://url1.com',
            'salary': {'from': 50000},
            'snippet': {'responsibility': 'Responsibility 1'}
        },
        {
            'name': 'Vacancy 2',
            'alternate_url': 'http://url2.com',
            'salary': None,
            'snippet': {'responsibility': 'Responsibility 2'}
        }
    ]
    vacancies = convert_to_vacancy_objects(vacancies_data)
    assert len(vacancies) == 2
    assert vacancies[0].title == "Vacancy 1"
    assert vacancies[0].salary == 50000
    assert vacancies[1].salary == 'Зарплата не указана'



def test_get_top_vacancies():
    vacancies = [
        Vacancy(title="Vacancy 1", url="http://url1.com", salary="50000", description="Description 1"),
        Vacancy(title="Vacancy 2", url="http://url2.com", salary="60000", description="Description 2")
    ]
    top_vacancies = get_top_vacancies(vacancies, 1)
    assert len(top_vacancies) == 1
    assert top_vacancies[0].title == "Vacancy 1"


def test_print_vacancies(capsys):
    vacancies = [
        Vacancy(title="Vacancy 1", url="http://url1.com", salary="50000", description="Description 1"),
        Vacancy(title="Vacancy 2", url="http://url2.com", salary="60000", description="Description 2")
    ]
    print_vacancies(vacancies)
    captured = capsys.readouterr()
    assert "Vacancy 1" in captured.out
    assert "Vacancy 2" in captured.out




