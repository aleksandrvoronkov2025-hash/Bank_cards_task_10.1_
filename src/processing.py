def filter_by_state(results_of_states: list, state: str = "EXECUTED") -> list:
    """Функция принимает:
    - список словарей;
    - опционально значение для ключа 'state' (по умолчанию 'EXECUTED');
    и возвращает:
    - новый список словарей, содержащий только те, у которых ключ 'state'соответствует
    указанному значению."""
    filtered_by_state = []
    for states in results_of_states:
        state_value = states.get('state', 'N/A')
        if state_value == state:
            filtered_by_state.append(states)
    return filtered_by_state


# Работа функции  filter_by_state:
results = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T081:33.419441'}]
print(filter_by_state(results))
print(filter_by_state(results, 'CANCELED'))


def filter_by_date(results_of_states: list, sort_in_decrease_order: str = 'True') -> list:
    """Функция принимает:
    - список словарей;
    - необязательный параметр, задающий порядок сортировки (по умолчанию — убывание);
    и возвращает:
    - новый список словарей, отсортированный по дате (date)"""

    from operator import itemgetter
    if not sort_in_decrease_order:
        sorted_by_date = sorted(results_of_states, key=itemgetter('date'), reverse=False)
    else:
        sorted_by_date = sorted(results_of_states, key=itemgetter('date'), reverse=True)
    return sorted_by_date


# Работа функции  filter_by_date:
sort = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_date(sort, "False"))
print(filter_by_date(sort, "True"))
print(filter_by_date(sort))
