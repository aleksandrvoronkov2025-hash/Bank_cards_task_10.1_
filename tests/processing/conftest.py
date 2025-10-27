import pytest

# 5. Тестирование функции filter_by_state.
# 5.1 Тестирование фильтрации списка словарей по заданному статусу state.
results = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
]

# 5.2 Проверка работы функции при отсутствии словарей с указанным статусом "state" в списке.
results_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T081:33.419441"},
]


@pytest.fixture
def filter_by_state_results():
    return results


# 6. Фикстуры тестирования функции sort_by_date:

# 6.1 Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.


@pytest.fixture
def normal_different_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# 6.2 Проверка корректности сортировки при одинаковых датах.
results_of_states_same_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T01:33.419441"},
]


@pytest.fixture
def same_date():
    return results_of_states_same_date


# 6.3 Тесты на работу функции с некорректными или нестандартными форматами дат.
results_of_states_incorrect_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2024/03/11T18:35:29:512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "0001-04-31T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2025-02-29T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2020-04-31T081:33.419441"},
    {"id": 594226725, "state": "CANCELED", "date": "2025-02-28T21:27:25.241689"},
    {"id": 594226711, "state": "CANCELED", "date": "2024-02-30T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2020-04-31T081:33.419441"},
    {"id": 594226725, "state": "CANCELED", "date": "2024-02-31T21:27:25.241689"},
    {"id": 594226711, "state": "CANCELED", "date": "2025-02-31T21:27:25.241689"},
]


@pytest.fixture
def incorrect_date():
    return results_of_states_incorrect_date
