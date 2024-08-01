def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return ""


def get_mask_account(account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    if len(account) == 25:
        return f"{'*' * 2}{account[-4:]}"
    else:
        return ""


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))
    print(get_mask_account("Счет 73654108430135874305"))
