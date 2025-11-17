import pytest

from src.generators import card_number_generator

# Тестирование функции card_number_generator


def test_card_number_generator_1(card_generator_1):
    start, end = card_generator_1
    card_number = card_number_generator(start=start, end=end)
    assert next(card_number) == "0000 0000 0000 0009"
    assert next(card_number) == "0000 0000 0000 0010"
    assert next(card_number) == "0000 0000 0000 0011"


def test_card_number_generator_2(card_generator_2):
    start, end = 9999999999999998, 9999999999999996
    card_number = card_number_generator(start=start, end=end)
    assert next(card_number) == "9999 9999 9999 9996"
    assert next(card_number) == "9999 9999 9999 9997"
    assert next(card_number) == "9999 9999 9999 9998"


def test_card_number_generator_3(card_generator_3):
    start, end = 0, 10000000000000000
    card_number = card_number_generator(start=start, end=end)
    assert next(card_number) == "Диапазон значений номеров карт указан неверно."


@pytest.mark.parametrize("start, end, expected", [(1, 1, "0000 0000 0000 0001"), (2, 2, "0000 0000 0000 0002")])
def test_card_number_generator_4(start, end, expected):
    assert (
        next(
            card_number_generator(
                start,
                end,
            )
        )
        == expected
    )


@pytest.mark.parametrize(
    "start, end, expected", [(1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])]
)
def test_card_number_generator_5(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


@pytest.mark.parametrize(
    "start, end, expected", [(3, 1, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])]
)
def test_card_number_generator_6(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


@pytest.mark.parametrize(
    "start, end, expected", [(0, 10000000000000000, "Диапазон значений номеров карт указан неверно.")]
)
def test_card_number_generator_7(start, end, expected):
    assert next(card_number_generator(start, end)) == expected


@pytest.mark.parametrize(
    "start, end, expected", [(0, 10000000000000000, ["Диапазон значений номеров карт указан неверно."])]
)
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected
