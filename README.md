# Course work with OOP

Я написала программу, которая будет получать информацию о вакансиях с платформы hh.ru в России, сохранять ее в файл и позволять удобно работать с ней: добавлять, фильтровать, удалять.

## Установка

### Предварительные требования

- Убедитесь, что у вас установлен Python (рекомендуется версия 3.8 или выше).
- Установите Poetry, если он еще не установлен. Вы можете установить его, следуя [официальной документации Poetry](https://python-poetry.org/docs/#installation).

### Шаги по установке

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Установите зависимости:**
Используйте Poetry для установки всех необходимых зависимостей:

   ```bash
    poetry install
    ```
   
3. **Активируйте виртуальную среду:**
Poetry автоматически создаст виртуальную среду для вашего проекта. Вы можете активировать её с помощью команды:

    ```bash
    poetry shell
    ```

4. **Запустите тесты:**
Вы можете запустить тесты с помощью следующей команды:

    ```bash
    poetry run pytest --cov=utils tests/ --cov-report=term
   ```


## Основные функции

1. **Абстрактный класс для работы с API**: абстрактный базовый класс Parser, который определяет интерфейс для всех парсеров вакансий. Включает абстрактные методы _connect_to_api для подключения к API и load_vacancies для загрузки вакансий.

2. **Класс для работы с API HeadHunter**: класс HH, который наследуется от Parser и реализует методы для подключения к API HeadHunter и загрузки вакансий. Включает приватные атрибуты для URL, заголовков, параметров запроса и списка вакансий.

3. **Класс для работы с вакансиями**: класс Vacancy, который представляет вакансию. Включает атрибуты title, url, salary, description и использует __slots__ для экономии памяти. Реализует методы сравнения вакансий по зарплате и валидацию данных при инициализации.

4. **Абстрактный класс для работы с файлами**: абстрактный базовый класс FileWorker, который определяет интерфейс для работы с файлами. Включает абстрактные методы add_vacancy для добавления вакансии в файл, get_vacancies для получения списка вакансий из файла и delete_vacancy для удаления вакансии из файла.

5. **Класс для работы с JSON-файлами**: класс JSONFileWorker, который наследуется от FileWorker и реализует методы для работы с JSON-файлами. Включает приватный атрибут для имени файла и методы для добавления, получения и удаления вакансий, а также проверку дубликатов при сохранении.

6. **Функции для взаимодействия с пользователем**: функция user_interaction, которая позволяет пользователю взаимодействовать с программой через консоль. Включает возможности для ввода поискового запроса, получения топ N вакансий по зарплате и фильтрации вакансий по ключевым словам.

7. **Вспомогательные функции**:
- Функция convert_to_vacancy_objects для преобразования списка словарей в список объектов Vacancy.
- Функция filter_vacancies для фильтрации вакансий по ключевым словам в описании.
- Функция get_vacancies_by_salary для фильтрации вакансий по зарплате в заданном диапазоне.
- Функция sort_vacancies для сортировки вакансий по зарплате.
- Функция get_top_vacancies для получения топ N вакансий.
- Функция print_vacancies для вывода информации о вакансиях в консоль.


## Использование

### Пример использования простых классов и функций

```python
from src.api_code import HH
from src.classes_vacancy import Vacancy, JSONFileWorker
from src.utils import convert_to_vacancy_objects, filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies

# Пример создания экземпляра класса для работы с API HeadHunter
hh_api = HH(JSONFileWorker())

# Получение вакансий с HeadHunter по ключевому слову
search_query = "Python Developer"
hh_api.load_vacancies(search_query)

# Преобразование данных в список объектов Vacancy
vacancies = convert_to_vacancy_objects(hh_api.vacancies)

# Пример фильтрации вакансий по ключевым словам
filter_words = ["разработка", "Python"]
filtered_vacancies = filter_vacancies(vacancies, filter_words)

# Пример фильтрации вакансий по зарплате
salary_range = "70000-120000"
ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

# Пример сортировки вакансий по зарплате
sorted_vacancies = sort_vacancies(ranged_vacancies)

# Пример получения топ N вакансий
top_n = 5
top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

# Пример вывода информации о вакансиях
print_vacancies(top_vacancies)

# Пример сохранения вакансии в JSON-файл
json_saver = JSONFileWorker()
vacancy = Vacancy(title="Senior Python Developer", 
                  url="https://hh.ru/vacancy/123456", 
                  salary="100000-150000", 
                  description="Требуется опыт работы от 5 лет.")
json_saver.add_vacancy(vacancy)

# Пример удаления вакансии из JSON-файла
json_saver.delete_vacancy(vacancy)
```


## Тестирование

В моем проекте используется тестирование для корректности работы. Я использовую фреймвор pytest.
Все написанные мною тесты находятся в папке tests.

```
File	             statements  missing  excluded  coverage
src\__init__.py	         0	    0	      0	      100%
src\api_code.py         30          2         0        93%
src\classes_vacancy.py  48	    9	      0	       81%
src\utils.py            63	   22	      0	       65%
Total                  141	   33	      0	       77%

```
