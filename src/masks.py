def get_mask_card_number(card_number: str = "0000000000000000") -> str:
    """Функция принимает на вход номер карты (строка из 16 цифр без пробелов) и
    возвращает ее маску в формате 'XXXX XX** **** XXXX'"""
    if card_number.isdigit() and len(card_number) == 16:
        substring_1 = card_number[0:4] + " "
        substring_2 = card_number[4:6] + "**" + " "
        substring_3 = "****" + " "
        substring_4 = card_number[-4:]
        mask_card_number = substring_1 + substring_2 + substring_3 + substring_4
    else:
        mask_card_number = "Номер карты указан неверно"
    return mask_card_number


def get_mask_account(account_number: str = "00000000000000000000") -> str:
    """Функция принимает на вход номер счета (строка из 20 цифр без пробелов) и
    возвращает его маску в формате '**XXXX' """
    if account_number.isdigit() and len(account_number) == 20:
        mask_account_number = "**" + account_number[-4:]
    else:
        mask_account_number = "Номер счета указан неверно"
    return mask_account_number
