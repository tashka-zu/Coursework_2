from src.api_code import HH
from src.classes_vacancy import JSONFileWorker, Vacancy


def convert_to_vacancy_objects(vacancies_data):
    """Преобразует список словарей в список объектов Vacancy"""
    vacancies = []
    for vacancy_data in vacancies_data:
        salary = None
        if "salary" in vacancy_data and vacancy_data["salary"]:
            salary = vacancy_data["salary"].get("from", None)

        vacancy = Vacancy(
            title=vacancy_data.get("name", ""),
            url=vacancy_data.get("alternate_url", ""),
            salary=salary,
            description=vacancy_data.get("snippet", {}).get("responsibility", ""),
        )
        vacancies.append(vacancy)
    return vacancies


def user_interaction():
    """Основная функция для взаимодействия с пользователем"""
    file_worker = JSONFileWorker()
    hh = HH(file_worker)

    search_query = input("Введите поисковый запрос: ")
    hh.load_vacancies(search_query)

    vacancies = convert_to_vacancy_objects(hh.vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")

    filtered_vacancies = filter_vacancies(vacancies, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


def filter_vacancies(vacancies, filter_words):
    """Фильтрует вакансии по ключевым словам в описании"""
    return [
        vacancy
        for vacancy in vacancies
        if vacancy.description and any(word.lower() in vacancy.description.lower() for word in filter_words)
    ]


def get_vacancies_by_salary(vacancies, salary_range):
    """Фильтрует вакансии по зарплате в заданном диапазоне"""
    if not salary_range:
        return vacancies

    min_salary, max_salary = map(int, salary_range.split("-"))

    def is_salary_in_range(vacancy):
        if vacancy.salary is None or isinstance(vacancy.salary, str) and "не указана" in vacancy.salary.lower():
            return False
        try:
            if isinstance(vacancy.salary, int):
                salary_value = vacancy.salary
            else:
                salary_value = int(vacancy.salary.split("-")[0].replace(" ", ""))
            return min_salary <= salary_value <= max_salary
        except ValueError:
            return False

    return [vacancy for vacancy in vacancies if is_salary_in_range(vacancy)]


def sort_vacancies(vacancies):
    """Сортирует вакансии по зарплате"""

    def get_salary_value(vacancy):
        if isinstance(vacancy.salary, int):
            return vacancy.salary
        elif isinstance(vacancy.salary, str) and "не указана" in vacancy.salary.lower():
            return 0
        else:
            try:
                return int(vacancy.salary.split("-")[0].replace(" ", ""))
            except ValueError:
                return 0

    return sorted(vacancies, key=get_salary_value, reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Возвращает топ N вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """Выводит информацию о вакансиях"""
    for vacancy in vacancies:
        print(f"Название: {vacancy.title}")
        print(f"Ссылка: {vacancy.url}")
        print(f"Зарплата: {vacancy.salary}")
        print(f"Описание: {vacancy.description}")
        print("-" * 40)
