from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функия для маскировки счетов и дат"""
    if "Счет" in card:
        mask_account = f"Счет {get_mask_account(card[:])}"
        return mask_account
    elif "Счет" not in card:
        numbers = get_mask_card_number(card[-16:])
        numbers_masks = card.replace(card[-16:], numbers)
        return numbers_masks
    else:
        return "Данные не правильны"


def get_data(info_data: str) -> str:
    """Функия преобразовывания даты и времени"""
    data_day = info_data.split("T")[0]

    return f"{data_day.split('-')[-1]}.{data_day.split('-')[-2]}.{data_day.split('-')[-3]}"

if __name__ == "__main__":
    print(mask_account_card("Счет 40817810224010345624"))
    print(get_data("2018 - 07 - 11T02: 26:18.671407"))
