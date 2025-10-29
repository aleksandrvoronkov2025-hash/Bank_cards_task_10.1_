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