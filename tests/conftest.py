import pytest

from src.masks import get_mask_account, get_mask_card_number


# 1. Фикстуры для тестирования функции get_mask_card_number:
# 1.1 Проверка маскирования карты с корректным номером (из 16 цифр).
@pytest.fixture
def card_number_1():
    return "7000792289606361"


@pytest.fixture
def card_number_2():
    return "1234567890123456"


@pytest.fixture
def card_number_3():
    return "3003792289606363"


@pytest.fixture
def card_number_4():
    return "4004792289606364"


@pytest.fixture
def card_number_5():
    return "5005792289606365"


@pytest.fixture
def card_number_6():
    return "6006792289606366"


@pytest.fixture
def card_number_0():
    return get_mask_card_number()


# 1.2 Проверка функции на различных неверных входных форматах номеров карт, включая граничные случаи
# и нестандартные длины номеров


@pytest.fixture
def card_number_7():
    return "12345678901234567"


@pytest.fixture
def card_number_8():
    return "123456789012345"


@pytest.fixture
def card_number_with_alpha():
    return "700079228960636a"


# 1.3 Проверка, что функция корректно обрабатывает входные строки, в которой отсутствует номер карты


@pytest.fixture
def card_number_empty_0():
    return ""


@pytest.fixture
def card_number_empty_space():
    return " "


@pytest.fixture
def card_number_00():
    return get_mask_card_number()


# 2. Фикстуры для тестирования функции get_mask_account:
# 2.1 Тестирование правильности маскирования номера счета (20 цифр)
@pytest.fixture
def get_mask_account_normal_1():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874301"


@pytest.fixture
def get_mask_account_normal_2():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874302"


@pytest.fixture
def get_mask_account_normal_3():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874303"


@pytest.fixture
def get_mask_account_normal_4():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874304"


@pytest.fixture
def get_mask_account_normal_5():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874305"


@pytest.fixture
def get_mask_account_normal_6():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874306"


@pytest.fixture
def get_mask_account_normal_7():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874307"


@pytest.fixture
def get_mask_account_normal_8():  # 20 цифр (нормированная длина номера счета)
    return "73654108430135874308"


# 2.2 Проверка работы функции с различными форматами и длинами номеров счетов.
@pytest.fixture
def get_mask_account_more():  # 21 цифра (+1 к нормированной длине номера счета)
    return "173654108430135874305"


@pytest.fixture
def get_mask_account_with_alpha():
    return "ф365410843013587430"  # 20 знаков с включением латиницы


# 2.3 Проверка, что функция корректно обрабатывает входные данные, где номер
# счета меньше ожидаемой длины
@pytest.fixture
def get_mask_account_less_1():
    return "7365410843013587430"  # 19 цифр (-1 от нормированной длины номера счета)


@pytest.fixture
def get_mask_account_less_2():
    return "736541084301358718"  # 18 цифр (-2 от нормированной длины номера счета)


@pytest.fixture
def get_mask_account_less_3():
    return "73654108430135817"  # 17 цифр (-3 от нормированной длины номера счета)


@pytest.fixture
def get_mask_account_less_4():
    return "7365410843013516"  # 16 цифр (-4 от нормированной длины номера счета)


@pytest.fixture
def get_mask_account_empty():
    return ""  # 0 знаков


@pytest.fixture
def get_mask_account_0():
    return get_mask_account()  # 0 знаков


# 3. Фикстуры тестирования функции mask_account_card модуля src.widget для:
# 3.1 Проверки, что функция mask_account_card корректно распознает и применяет нужный тип
# маскировки в зависимости от типа входных данных (карта или счет).
@pytest.fixture
def mask_card_visa_platinum():
    return "Visa Platinum 7000792289606361"  # Карта Visa Platinum


@pytest.fixture
def mask_card_maestro():
    return "Maestro 1234567890123456"  # Карта Maestro


@pytest.fixture
def mask_account():
    return "Счет 73654108430135874305"  # Счет


# 3.3 Тестирования функции mask_account_card на обработку некорректных входных данных
# и проверка ее устойчивости к ошибкам.
@pytest.fixture
def mask_account_error_alpha_1():
    return "Счет 7365410843013587430a"  # В счете последняя цифра заменена на букву


@pytest.fixture
def mask_account_error_alpha_2():
    return "Сче  7365410843013587430a"  # В слове "счет" пропущена последняя буква, заменена последняя цифра на букву


@pytest.fixture
def mask_card_error_alpha():
    return "aestro 7000792289606361"  # Недопустимое имя карты


@pytest.fixture
def mask_card_error_number():
    return "Maestro 70007922896063611"  # Недопустимый номер карты


@pytest.fixture
def mask_card_error_number_alpha():
    return "Maestr 70007922896063611"  # Недопустимые имя и номер карты


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
