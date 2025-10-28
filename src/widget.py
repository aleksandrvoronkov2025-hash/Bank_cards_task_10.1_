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
        name_card = card[0:name_length - 1]
        if card_number_length == 16 and name_card.lower() in card_names_variants:
            mask_card_number = masks.get_mask_card_number(card_number)
            mask = name_card + " " + mask_card_number
        # Значение функции для всех прочих случаев ввода данных, не соответствующих ожидаемым форматам
        else:
            mask = "Введены некорректные данные карты или счета"
    return mask


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date: str = "2024-03-11T02:26:18.671407") -> str:
    """Функция, которая одной строкой:
    -принимает на вход дату и время в формате 'ГГ-ММ-ДДTЧЧ:ММ:СС.х'('2024-03-11T02:26:18.671407');
    -возвращает дату в формате 'ДД.ММ.ГГГГ' ('11.03.2024') """
    date_data = [date[8:10], date[5:7], date[0:4]]
    date = ".".join(date_data)
    return date


print(get_date("2024-03-11T02:26:18.671407"))
