import pytest

from src.widget import get_date, mask_account_card

# 3. Тестирование функции get_mask_account из модуля tests.conftest.py

# 3.1 Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости
# от типа входных данных (карта или счет).


def test_get_mask_card_visa_platinum(mask_card_visa_platinum):
    assert mask_account_card(mask_card_visa_platinum) == "Visa Platinum 7000 79** **** 6361"


def test_get_mask_card_maestro(mask_card_maestro):
    assert mask_account_card(mask_card_maestro) == "Maestro 1234 56** **** 3456"


def test_get_mask_account(mask_account):
    assert mask_account_card(mask_account) == "Счет **4305"


# 3.2 Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.


@pytest.mark.parametrize(
    "card_account_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(card_account_number, expected):
    assert mask_account_card(card_account_number) == expected


# 3.3 Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.


def test_mask_account_error_alpha_1(mask_account_error_alpha_1):
    assert mask_account_card(mask_account_error_alpha_1) == "Введены некорректные данные карты или счета"


def test_mask_account_error_alpha_2(mask_account_error_alpha_2):
    assert mask_account_card(mask_account_error_alpha_2) == "Введены некорректные данные карты или счета"


def test_mask_card_error_alpha(mask_card_error_alpha):
    assert mask_account_card(mask_card_error_alpha) == "Введены некорректные данные карты или счета"


def test_mask_card_error_number(mask_card_error_number):
    assert mask_account_card(mask_card_error_number) == "Введены некорректные данные карты или счета"


# 4. Параметризованные тесты функции get_date:


# 4.1 Тестирование правильности преобразования даты
@pytest.mark.parametrize(
    "date_normal, expected",
    [
        ("2024-02-28T02:26:18.671407", "28.02.2024"),
        ("2023-11-25T02:26:18.671408", "25.11.2023"),
        ("2024-06-11 T02:26:18.671407", "11.06.2024"),
        ("2024-07-11 T02:26:18", "11.07.2024"),
        ("2024-12-31T02:26:18.671407", "31.12.2024"),
        ("2025-03-30T02", "30.03.2025"),
        ("2024.12.31", "31.12.2024"),
    ],
)
def test_get_date_norm_1(date_normal, expected):
    assert get_date(date_normal) == expected


# 4.2 Проверка работы функции get_date на различных входных форматах даты,
# включая граничные случаи и нестандартные строки с датами.
@pytest.mark.parametrize(
    "date_error_noise, expected",
    [
        ("2024ю03ю11T02ж26ж18ю671407", "11.03.2024"),
        ("0001-04-31T02:26:18.671407", "Нет корректных календарных данных"),
        ("2024-02-29", "Нет корректных календарных данных"),
        ("2025-02-29", "Нет корректных календарных данных"),
        ("2020/02/30", "Нет корректных календарных данных"),
    ],
)
def test_get_date_norm_2(date_error_noise, expected):
    assert get_date(date_error_noise) == expected


# 4.3 Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
@pytest.mark.parametrize(
    "date_no, expected",
    [
        ("0000-10-31T02:26:18.671407", "Нет корректных календарных данных"),
        ("0001-05-32T02:26:18.671407", "Нет корректных календарных данных"),
        ("000ы-11-31T02:26:18.671407", "Нет корректных календарных данных"),
        ("000ю03ю11T02ж26ж18ю67140", "Нет корректных календарных данных"),
    ],
)
def test_get_date_norm(date_no, expected):
    assert get_date(date_no) == expected
