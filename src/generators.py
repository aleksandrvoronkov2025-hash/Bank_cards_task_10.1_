
transactions_1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount_": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 939719571,
        "state": "EXECUTED",
        "date": "2019-07-30T02:07:58.425572",
        "operationAmount": {"amount": "20000.07", "currency_": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916953",
        "to": "Счет 11776614605963066704",
    },
]

transactions_2 = [
    {
        "id": 939719572,
        "state": "EXECUTED",
        "date": "2020-06-30T02:09:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод частному лицу",
        "from": "Счет 75106830613657916957",
        "to": "Счет 11776614605963066708",
    },
    {
        "id": 939719573,
        "state": "EXECUTED",
        "date": "2020-07-30T02:10:58.425572",
        "operationAmount": {"amount": "7000.07", "currency": {"name": "CNY", "code": "CNY"}},
        "description": "Перевод другану",
        "from": "Счет 75106830613657916923",
        "to": "Счет 11776614605963066826",
    },
]

transactions_4 = []

transactions_5 = [
                {
                    "id": 939719571,
                    "state": "EXECUTED",
                    "date": "2019-07-30T02:07:58.425572",
                    "operationAmount": {"amount": "20000.07", "currency": {"name": "CNY", "code": "CNY"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916953",
                    "to": "Счет 11776614605963066704"
                }]

def filter_by_currency(transactions, currency_type: str = "USD"):
    """Функция-генератор "filter_by_currency", которая:
    - принимает список словарей, представляющих транзакции, и тип валюты операции (по умолчанию - "USD")
    - поочередно выдает транзакции с заданным типом валюты транзакции"""
    if transactions:
        for transaction in transactions:
            operation_amount = transaction.get("operationAmount", {})
            currency_dictionary = operation_amount.get("currency", {})
            currency_code = currency_dictionary.get("code", "")
            if currency_code == currency_type:
                yield transaction
            else:
                if operation_amount == {}:
                    yield ["ключ 'operationAmount' о размере и валюте транзакции не найден"]
                if operation_amount != {} and currency_dictionary == {}:
                    yield ["искомый словарь транзакции 'currency' не найден"]
                if currency_dictionary != {} and currency_code != currency_type:
                    yield ["искомая валюта транзакций не найдена"]
    else:
        yield ["список транзакций не найден"]


filter_current = filter_by_currency(transactions_1)
print(next(filter_current))
print(next(filter_current))
print(next(filter_current))

filter_current = filter_by_currency(transactions_2, "CNY")
print(next(filter_current))
#print(next(filter_current))

filter_current = filter_by_currency(transactions_4)
print(next(filter_current))

filter_current = filter_by_currency(transactions_5, "USD")
print(next(filter_current))
print()

def transaction_descriptions(transactions):
    """Функция-генератор transaction_descriptions, которая:
     - принимает список словарей с транзакциями;
     - возвращает описание каждой операции по очереди"""
    if transactions:
        for transaction in transactions:
            descript = transaction.get("description", "")
            if descript != "":
                yield [descript]
            else:
                yield ["сведения об операции не найдены"]
    else:
        yield ["список транзакций пустой"]

description = transaction_descriptions(transactions_1)
for i in range(3):
    print(next(description))

#description = transaction_descriptions(transactions_1)
#print(next(description))
#print(next(description))
#print(next(description))

description = transaction_descriptions(transactions_2)
for i in range(2):
    print(next(description))

description = transaction_descriptions([])
print(next(description))

#description = transaction_descriptions(transactions_2)
#print(next(description))
#print(next(description))
print()

def card_number_generator(start=1, end=9999999999999999):
    """Функция-генератор 'card_number_generator', которая выдает номера
    банковских карт в формате  'XXXX XXXX XXXX XXXX'.
    Генератор может сгенерировать номера в диапазоне
    0000 0000 0000 0001 - 9999 9999 9999 9999"""
    mask_number = "Диапазон значений номеров карт указан неверно."
    if 1 <= start <= 9999999999999999 and 9999999999999999 >= end >= 1:
        if start > end:
            a=start
            b=end
            start=b
            end=a
        for i in range(start, end + 1):
            end_number_card = i
            end_number_card = str(end_number_card)
            mask = "0"
            if len(end_number_card) < 16:
                mask_string = (16 - len(end_number_card)) * mask
                mask_number = mask_string + end_number_card
            else:
                mask_number = end_number_card
            mask_number = mask_number[:4] + " " + mask_number[4:]
            mask_number = mask_number[:9] + " " + mask_number[9:]
            mask_number = mask_number[:14] + " " + mask_number[14:]
            yield mask_number
    else:
        yield mask_number



card_number = card_number_generator(9, 11)
for i in range(3):
    print(next(card_number))

#card_number = card_number_generator(9, 11)
#print(next(card_number))
#print(next(card_number))
#print(next(card_number))

card_number = card_number_generator(9999999999999998, 9999999999999996)
for i in range(3):
    print(next(card_number))

#card_number = card_number_generator(9999999999999998, 9999999999999996)
#print(next(card_number))
#print(next(card_number))
#print(next(card_number))

#card_number = card_number_generator(99999999999999989, 99999999999999969)
#for i in range(1):
#    print(next(card_number))

card_number = card_number_generator(99999999999999989, 99999999999999969)
print(next(card_number))
