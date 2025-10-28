import pytest


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
