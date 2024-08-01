from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(mask_card_number, expected):
    assert get_mask_card_number('700092289606361') == '7000 79** **** 6361'

    assert get_mask_card_number('70009228960636') == ''


def test_get_mask_account(mask_account, expected):
    assert get_mask_account('73654108430135874305') == '**4305'
