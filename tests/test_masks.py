import pytest

from src.masks import get_mask_account, get_mask_card_number


# 1. Тестирование функции get_mask_card_number через фикстуры из модуля tests.conftest.py:
# 1.1 Проверка маскирования карты с корректным номером (из 16 цифр).
def test_get_mask_card_number_1(card_number_1):
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"


def test_get_mask_card_number_2(card_number_2):
    assert get_mask_card_number(card_number_2) == "1234 56** **** 3456"


def test_get_mask_card_number_3(card_number_3):
    assert get_mask_card_number(card_number_3) == "3003 79** **** 6363"


def test_get_mask_card_number_4(card_number_4):
    assert get_mask_card_number(card_number_4) == "4004 79** **** 6364"


def test_get_mask_card_number_5(card_number_5):
    assert get_mask_card_number(card_number_5) == "5005 79** **** 6365"


def test_get_mask_card_number_6(card_number_6):
    assert get_mask_card_number(card_number_6) == "6006 79** **** 6366"


# 1.2 Проверка функции на различных неверных входных форматах номеров карт, включая граничные случаи и нестандартные
# длины номеров
def test_get_mask_card_number_7(card_number_7):
    assert get_mask_card_number(card_number_7) == "Номер карты указан неверно"


def test_get_mask_card_number_8(card_number_8):
    assert get_mask_card_number(card_number_8) == "Номер карты указан неверно"


def test_get_mask_card_with_alpha(card_number_with_alpha):
    assert get_mask_card_number(card_number_with_alpha) == "Номер карты указан неверно"


# 1.3 Проверка, что функция корректно обрабатывает входные строки, в которых отсутствует номер карты
def test_get_mask_card_empty_0(card_number_empty_0):
    assert get_mask_card_number(card_number_empty_0) == "Номер карты указан неверно"


def test_get_mask_card_empty_space(card_number_empty_space):
    assert get_mask_card_number(card_number_empty_space) == "Номер карты указан неверно"


def test_get_mask_card_number_0(card_number_00):
    assert get_mask_card_number() == "0000 00** **** 0000"


# 2. Тестирование функции get_mask_account через фикстуры из модуля tests.conftest.py
# 2.1 Тестирование правильности маскирования номера счета ожидаемой длины и содержания (20 цифр)
def test_get_mask_account_normal_1(get_mask_account_normal_1):
    assert get_mask_account(get_mask_account_normal_1) == "**4301"


def test_get_mask_account_normal_2(get_mask_account_normal_2):
    assert get_mask_account(get_mask_account_normal_2) == "**4302"


def test_get_mask_account_normal_3(get_mask_account_normal_3):
    assert get_mask_account(get_mask_account_normal_3) == "**4303"


def test_get_mask_account_normal_4(get_mask_account_normal_4):
    assert get_mask_account(get_mask_account_normal_4) == "**4304"


def test_get_mask_account_normal_5(get_mask_account_normal_5):
    assert get_mask_account(get_mask_account_normal_5) == "**4305"


def test_get_mask_account_normal_6(get_mask_account_normal_6):
    assert get_mask_account(get_mask_account_normal_6) == "**4306"


def test_get_mask_account_normal_7(get_mask_account_normal_7):
    assert get_mask_account(get_mask_account_normal_7) == "**4307"


def test_get_mask_account_normal_8(get_mask_account_normal_8):
    assert get_mask_account(get_mask_account_normal_8) == "**4308"


# 2.2 Проверка работы функции с различными форматами и длинами номеров счетов.
def test_get_mask_account_more(get_mask_account_more):
    assert get_mask_account(get_mask_account_more) == "Номер счета указан неверно"


def test_get_mask_account_with_alpha(get_mask_account_with_alpha):
    assert get_mask_account(get_mask_account_with_alpha) == "Номер счета указан неверно"


# 2.3 Проверка, что функция корректно обрабатывает входные данные, где номер счета
# меньше ожидаемой длины


def test_get_mask_account_less_1(get_mask_account_less_1):
    assert get_mask_account(get_mask_account_less_1) == "Номер счета указан неверно"


def test_get_mask_account_less_2(get_mask_account_less_2):
    assert get_mask_account(get_mask_account_less_2) == "Номер счета указан неверно"


def test_get_mask_account_less_3(get_mask_account_less_3):
    assert get_mask_account(get_mask_account_less_3) == "Номер счета указан неверно"


def test_get_mask_account_less_4(get_mask_account_less_4):
    assert get_mask_account(get_mask_account_less_4) == "Номер счета указан неверно"


def test_get_mask_account_empty(get_mask_account_empty):
    assert get_mask_account(get_mask_account_empty) == "**0000"


def test_get_mask_account_0(get_mask_account_0):
    assert get_mask_account() == "**0000"


@pytest.mark.parametrize(
    "account_number_1, expected",
    [
        ("7365410843013587430", "Номер счета указан неверно"),
        ("", "**0000"),
        ("12345678901234567890", "**7890"),
        ("09876543210987654321", "**4321"),
        ("00000000000000000000", "**0000"),
        ("a000000000000000000a", "Номер счета указан неверно"),
    ],
)
def test_get_mask_account_1_parametrize(account_number_1, expected):
    assert get_mask_account(account_number_1) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("asdfghjkl;qwertyuiop", "Номер счета указан неверно"),
        ("", "**0000"),
        ("12345678904589675432", "**5432"),
        ("09876543210987654321", "**4321"),
        ("12345678901234560000", "**0000"),
        ("3562396527806543290755", "Номер счета указан неверно"),
    ],
)
def test_get_mask_account_parametrize(account_number, expected):
    assert get_mask_account(account_number) == expected
