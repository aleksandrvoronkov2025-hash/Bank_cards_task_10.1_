import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(currency_1):
    generator = filter_by_currency(currency_1, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == ["ключ 'operationAmount' о размере и валюте транзакции не найден"]
    assert next(generator) == ["искомый словарь транзакции 'currency' не найден"]


def test_filter_by_currency_1(currency_1):
    generator = filter_by_currency(currency_1)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == ["ключ 'operationAmount' о размере и валюте транзакции не найден"]
    assert next(generator) == ["искомый словарь транзакции 'currency' не найден"]
    assert next(generator) == ["ключ 'operationAmount' о размере и валюте транзакции не найден"]


def test_filter_by_currency_2(currency_2):
    generator = filter_by_currency(currency_2, "CNY")
    assert next(generator) == ["искомая валюта транзакций не найдена"]
    assert next(generator) == {
        "id": 939719573,
        "state": "EXECUTED",
        "date": "2020-07-30T02:10:58.425572",
        "operationAmount": {"amount": "7000.07", "currency": {"name": "CNY", "code": "CNY"}},
        "description": "Перевод другану",
        "from": "Счет 75106830613657916923",
        "to": "Счет 11776614605963066826",
    }


expected_1 = [
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ],
    "ключ 'operationAmount' о размере и валюте транзакции не найден",
    "искомый словарь транзакции 'currency' не найден",
    "ключ 'operationAmount' о размере и валюте транзакции не найден",
]


@pytest.mark.parametrize(
    "transactions, currency_type, expected",
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
            "USD",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        )
    ],
)
def test_filter_by_currency_3(transactions, currency_type, expected):
    assert (next(filter_by_currency(
                [
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                        "from": "Счет 75106830613657916952",
                        "to": "Счет 11776614605963066702",
                    }
                ]
            )
        )
        == expected
    )




@pytest.mark.parametrize(
    "transactions, currency_type, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "USD",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        ),
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount_": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            "USD",
            ["ключ 'operationAmount' о размере и валюте транзакции не найден"],
        ),
        (
            [
                {
                    "id": 939719571,
                    "state": "EXECUTED",
                    "date": "2019-07-30T02:07:58.425572",
                    "operationAmount": {"amount": "20000.07", "currency_": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916953",
                    "to": "Счет 11776614605963066704",
                }
            ],
            "USD", ["искомый словарь транзакции 'currency' не найден"]), ([],"USD", ["список транзакций не найден"]), (
            [
                {
                    "id": 939719571,
                    "state": "EXECUTED",
                    "date": "2019-07-30T02:07:58.425572",
                    "operationAmount": {"amount": "20000.07", "currency": {"name": "CNY", "code": "CNY"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916953",
                    "to": "Счет 11776614605963066704"
                }], "CNY", ["искомая валюта транзакций не найдена"])])
def test_filter_by_currency_4(transactions, currency_type, expected):
    assert next(filter_by_currency(transactions, "USD")) == expected
