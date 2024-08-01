import pytest
from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Счет 408178102240103456245", "Счет **6245"),
        ("Visa Classic 4256234567819034", "Visa Classic 4256 23** **** 9034"),
        ("МИР 2202202467890987", "МИР 2202 20** **** 0987")
    ]
)

def test_mask_account_card(account_card, expected):
    assert mask_account_card("Счет 40817810224010345624") == "Счет **5624"


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", ' 11. 07 .2018 '),
        ("2023-05-23T03:25:11.234567", "23.05.2023"),
        ("2024-01-01T01:19:23:456982", "01.01.2024")
    ]
)

def test_get_date(input_date, expected):
    assert get_data("2018 - 07 - 11T02: 26:18.671407") == ' 11. 07 .2018 '
