def mask_account_card(card: str = "Cчет 00000000000000000000") -> str:
    """Функция, которая одной строкой:
    -принимает 'тип' и номер карты из 16 цифр или 'счет' с номером из 20 цифр;
    -возвращает полученные данные в маскированном виде:
    "'тип карты''XXXX XX** **** XXXX'
    'счет **XXXX'"""
    # Импортируем файл с функциями маскирования номеров карты и счета
    from src import masks

    # Проверка принадлежности данных строки к счету с последующим его маскированием
    score = card[0:4]
    score_number = card[-20:]
    if len(card) == 25 and score.lower() == "счет" and score_number.isdigit():
        mask_account_number = masks.get_mask_account(score_number)
        mask = "Счет " + mask_account_number
    else:
        # Проверка принадлежности данных строки к карте с последующим маскированием
        card_names_variants = ["visa platinum", "maestro"]
        card_number = card[-16:]
        card_number_length = len(card_number)
        name_length = len(card) - 16
        name_card = card[0 : name_length - 1]
        if card_number_length == 16 and name_card.lower() in card_names_variants:
            mask_card_number = masks.get_mask_card_number(card_number)
            mask = name_card + " " + mask_card_number
        # Значение функции для всех прочих случаев ввода данных, не соответствующих ожидаемым форматам
        else:
            mask = "Введены некорректные данные карты или счета"
    return mask


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 1234567890123456"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date: str = "2024-03-11T02:26:18.671407") -> str:
    """Функция, которая одной строкой:
    -принимает на вход дату и время в формате 'ГГ-ММ-ДДTЧЧ:ММ:СС.х'('2024-03-11T02:26:18.671407');
    -возвращает дату в формате 'ДД.ММ.ГГГГ' ('11.03.2024')"""

    date_data = [date[8:10], date[5:7], date[0:4]]
    day = date_data[0]
    month = date_data[1]
    year = date_data[2]

    # Максимальное количество дней в календарных месяцах
    calendar = {1: 31, 2: 28, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Счетчик ошибок для фиксации несоответствия данных календарной дате
    date_1 = 0
    if (
        day.isdigit()
        and month.isdigit()
        and year.isdigit()
        and len(year) == 4
        and len(month) == 2
        and len(day) == 2
        and 1 <= int(day) <= 31
        and 1 <= int(month) <= 12
        and 1 <= int(year)
    ):
        max_days_month = calendar.get(int(month), 0)
        if int(year) % 4 == 0:
            leap_year = True
        else:
            leap_year = False
        if int(month) == 2 and int(day) == 29 and leap_year:
            date_1 += 1
        if int(month) == 2 and int(day) > 28 and not leap_year:
            date_1 += 1
        if int(month) == 2 and 29 < int(day) <= 31:
            date_1 += 1
        if int(month) == 2 and 29 < int(day) <= 31:
            date_1 += 1
        if int(day) <= int(max_days_month) and int(date_1) == 0:
            date_ = ".".join(date_data)
        else:
            date_ = "Нет корректных календарных данных"
    else:
        date_ = "Нет корректных календарных данных"
    return date_


print(get_date("2024-02-28T02:26:18.671407"))
print(get_date("2023-11-25T02:26:18.671408"))
print(get_date("2024-06-11 T02:26:18.671407"))
print(get_date("2024-07-11 T02:26:18"))
print(get_date("2024-12-31T02:26:18.671407"))
print(get_date("2025-03-30T02"))
print(get_date("2024.12.31"))

print(get_date("2024ю03ю11T02ж26ж18ю671407"))
print(get_date("0001-04-31T02:26:18.671407"))
print(get_date("2024-02-29"))
print(get_date("2025-02-29"))
print(get_date("2020/02/30"))

print(get_date("0000-10-31T02:26:18.671407"))
print(get_date("0001-05-32T02:26:18.671407"))
print(get_date("000ы-11-31T02:26:18.671407"))
print(get_date("000ю03ю11T02ж26ж18ю671407"))
