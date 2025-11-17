# Проект "Виджет банковских операций клиента"

## Описание:

Проект является бэкендом для клиентского приложения банка.

## Тестирование:
Содержит пакет tests для тестирования 4-х модулей (с функциями):
masks, processing, widget и добавленным вновь generators

## Установка:

1. Клонируйте репозиторий
https://github.com/aleksandrvoronkov2025-hash/Bank_cards_task_10.1_
2. Установите зависимости:
pip install -r requirements.txt

## Использование:
Примеры использования функций-генераторов из модуля "generators".
1. Функция "filter_by_currency":
filter_current = filter_by_currency(transactions_1)
print(next(filter_current))
print(next(filter_current))
print(next(filter_current))

{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
["ключ 'operationAmount' о размере и валюте транзакции не найден"]
["искомый словарь транзакции 'currency' не найден"]

2. Функция "card_number_generator":
card_number = card_number_generator(9, 11)
for i in range(3):
    print(next(card_number))
0000 0000 0000 0009
0000 0000 0000 0010
0000 0000 0000 0011

card_number = card_number_generator(9999999999999998, 9999999999999996)
for i in range(3):
    print(next(card_number))
9999 9999 9999 9996
9999 9999 9999 9997
9999 9999 9999 9998

card_number = card_number_generator(99999999999999989, 99999999999999969)
Диапазон значений номеров карт указан неверно.

3. Функция "transaction_descriptions":
description = transaction_descriptions(transactions_1)
for i in range(3):
    print(next(description))
['Перевод организации']
['Перевод со счета на счет']
['Перевод организации']

description = transaction_descriptions(transactions_2)
for i in range(2):
    print(next(description))
['Перевод частному лицу']
['Перевод другану']

description = transaction_descriptions([])
print(next(description))
['список транзакций пустой']

## Документация и ссылки

## Лицензия