import pytest

from src.generators import transaction_descriptions


def test_transaction_descriptions_1(description_1):
    description = transaction_descriptions(description_1)
    assert next(description) == ["Перевод организации"]
    assert next(description) == ["Перевод со счета на счет"]
    assert next(description) == ["Перевод организации"]


def test_transaction_descriptions_2(description_2):
    description = transaction_descriptions(description_2)
    assert next(description) == ["Перевод частному лицу"]
    assert next(description) == ["Перевод другану"]


def test_transaction_descriptions_3(description_3):
    description = transaction_descriptions(description_3)
    assert next(description) == ["Перевод на СВО"]
    assert next(description) == ["Перевод со счета на счет"]
    assert next(description) == ["сведения об операции не найдены"]
    assert next(description) == ["сведения об операции не найдены"]

def test_transaction_descriptions_4(description_4):
    description = transaction_descriptions(description_4)
    assert next(description) == ["список транзакций пустой"]

@pytest.mark.parametrize(
    "transaction, expected",
    [
        (
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            ["Перевод организации"],
        ),
        (
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount_": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            ["Перевод со счета на счет"],
        ),
        (
            {
                "id": 939719571,
                "state": "EXECUTED",
                "date": "2019-07-30T02:07:58.425572",
                "operationAmount": {"amount": "20000.07", "currency_": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916953",
                "to": "Счет 11776614605963066704",
            },
            ["Перевод организации"],
        ),
    ],
)
def test_transaction_descriptions(transaction, expected):
    assert next(transaction_descriptions([transaction])) == expected
