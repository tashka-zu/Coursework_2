from unittest.mock import patch

from src.api_code import HH


def test_hh_load_vacancies():
    """Тестирует метод load_vacancies класса HH"""
    hh = HH(file_worker=None)

    with patch("src.api_code.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "items": [
                {
                    "name": "Test Vacancy",
                    "alternate_url": "http://test.url",
                    "salary": {"from": 50000},
                    "snippet": {"responsibility": "Test responsibility"},
                }
            ]
        }

        hh.load_vacancies("test")

        assert len(hh.vacancies) == 20
        assert all(vacancy["name"] == "Test Vacancy" for vacancy in hh.vacancies)
