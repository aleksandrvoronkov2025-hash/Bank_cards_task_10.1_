import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import results, results_1

# 5. Тестирование функции filter_by_state
# 5.1 Тестирование фильтрации списка словарей по заданному статусу state.


def test_filter_by_state_cancel(filter_by_state_results):
    assert filter_by_state(results, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
    ]


# 5.2 Проверка работы функции при отсутствии словарей с указанным статусом 'state' в списке.


def test_filter_by_not_state_1(filter_by_state_results):
    assert filter_by_state(results_1, "CANCEL") == []


def test_filter_by_not_state_2(filter_by_state_results):
    assert filter_by_state(results_1, "CANCELED") == []


# 5.3 Параметризация тестов для различных возможных значений статуса 'state'.

input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
]

output_data_by_executed = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
output_data_by_canceled = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
]
output_data_by_other = []


@pytest.mark.parametrize(
    "input_data, status, expected_result",
    [
        (input_data, "EXECUTED", output_data_by_executed),
        (input_data, "CANCELED", output_data_by_canceled),
        (input_data, "other", output_data_by_other),
    ],
)
def test_filter_by_state(input_data, status, expected_result):
    assert filter_by_state(input_data, status) == expected_result


# 6. Тестирование функции sort_by_date:

# 6.1 Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.


def test_sort_by_date_1(normal_different_date):
    assert sort_by_date(normal_different_date, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_2(normal_different_date):
    assert sort_by_date(normal_different_date, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_3(normal_different_date):
    assert sort_by_date(normal_different_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# 6.2 Проверка корректности сортировки при одинаковых датах.
def test_sort_by_date_4(same_date):
    assert sort_by_date(same_date, True) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T01:33.419441"},
    ]


def test_sort_by_date_5(same_date):
    assert sort_by_date(same_date, False) == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T01:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:58.425572"},
    ]


def test_sort_by_date_6(same_date):
    assert sort_by_date(same_date) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T01:33.419441"},
    ]


# 6.3 Тесты на работу функции с некорректными или нестандартными форматами дат.
def test_sort_by_date_7(incorrect_date):
    assert sort_by_date(incorrect_date, True) == [
        {"id": 594226725, "state": "CANCELED", "date": "2025-02-28T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2024/03/11T18:35:29:512364"},
    ]


def test_sort_by_date_8(incorrect_date):
    assert sort_by_date(incorrect_date, False) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2024/03/11T18:35:29:512364"},
        {"id": 594226725, "state": "CANCELED", "date": "2025-02-28T21:27:25.241689"},
    ]


def test_sort_by_date_9(incorrect_date):
    assert sort_by_date(incorrect_date) == [
        {"id": 594226725, "state": "CANCELED", "date": "2025-02-28T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2024/03/11T18:35:29:512364"},
    ]
