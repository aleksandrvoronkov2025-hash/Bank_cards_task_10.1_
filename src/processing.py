def filter_by_state(results_of_states: list, state: str = "EXECUTED") -> list:
    """Функция принимает:
    - список словарей;
    - опционально значение для ключа 'state' (по умолчанию 'EXECUTED');
    и возвращает:
    - новый список словарей, содержащий только те, у которых ключ 'state'соответствует
    указанному значению."""
    filtered_by_state = []
    for states in results_of_states:
        state_value = states.get("state", "N/A")
        if state_value == state:
            filtered_by_state.append(states)
    return filtered_by_state


# Работа функции  filter_by_state:
results = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
]


# print(filter_by_state(results))
# print(filter_by_state(results, 'CANCELED'))
# print(filter_by_state(results, 'CANCEL'))


def sort_by_date(results_of_states: list, sort_in_decrease_order: bool = True) -> list:
    """Функция принимает:
    - список словарей;
    - необязательный параметр, задающий порядок сортировки (по умолчанию — убывание);
    и возвращает:
    - новый список словарей, отсортированный по дате (date)"""

    # Новый список словарей с проверенными данными датами.
    results_of_states_with_clear_date = []
    sorted_by_date = ["Нет корректных календарных данных"]
    # Максимальное количество дней в календарных месяцах
    calendar = {1: 31, 2: 28, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for dictionary in results_of_states:
        # Извлечение данных о дате из текущего словаря списка
        date_operation = dictionary.get("date")
        #    print(dictionary)
        date_data = [date_operation[0:4], date_operation[5:7], date_operation[8:10]]
        day = date_data[2]
        month = date_data[1]
        year = date_data[0]
        #        date_ = ".".join(date_data)
        #        print(date_)
        # Проверка корректности данных о дате из текущего словаря списка
        date_ = "Дата корректная"  # Значение о состоянии даты по умолчанию
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
            and date_operation != "Нет корректных календарных данных"
        ):
            date_1 = 0  # счетчик некорректных данных о дате
            max_days_month = calendar.get(int(month), 0)
            if int(year) % 4 == 0:
                leap_year = True
            else:
                leap_year = False
            if int(month) == 2 and int(day) == 29 and not leap_year:
                date_1 += 1
            if int(month) == 2 and 29 < int(day) <= 31:
                date_1 += 1
            if max_days_month < int(day) or date_1 != 0:
                date_ = "Нет корректных календарных данных"
        #                print(date_)
        if date_ != "Нет корректных календарных данных":
            #            print(date_)
            results_of_states_with_clear_date.append(dictionary)
    #    print(results_of_states_with_clear_date)
    # Импортирование встроенных инструментов для работы с датами
    from operator import itemgetter

    # Сортировка заполненного словаря по дате
    if len(results_of_states_with_clear_date) != 0:
        if sort_in_decrease_order:
            sorted_by_date = sorted(results_of_states_with_clear_date, key=itemgetter("date"), reverse=True)
        else:
            sorted_by_date = sorted(results_of_states_with_clear_date, key=itemgetter("date"), reverse=False)
    return sorted_by_date


# Работа функции  sort_by_date:

# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
results_of_states_different_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T081:33.419441"},
]  # print(sort_by_date(results_of_states_different_date, True))
print(sort_by_date(results_of_states_different_date, True))
print(sort_by_date(results_of_states_different_date, False))
print(sort_by_date(results_of_states_different_date))

# Проверка корректности сортировки при одинаковых датах.
results_of_states_same_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:36:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T01:33.419441"},
]
print(sort_by_date(results_of_states_same_date, True))
print(sort_by_date(results_of_states_same_date, False))
print(sort_by_date(results_of_states_same_date))
# Тесты на работу функции с некорректными или нестандартными форматами дат.

results_of_states_uncorrect_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2024/03/11T18:35:29:512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "0001-04-31T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2025-02-29T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2020-04-31T081:33.419441"},
]
#print(sort_by_date(results_of_states_uncorrect_date, True))
#print(sort_by_date(results_of_states_uncorrect_date, False))
#print(sort_by_date(results_of_states_uncorrect_date))
