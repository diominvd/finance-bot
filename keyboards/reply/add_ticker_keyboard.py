from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lines import keyboards_lines


def create_add_ticker_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards_lines['add_ticker_keyboard']['cancel']),
        ]
    ]
    add_ticker_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                              keyboard=keyboard_buttons)

    return add_ticker_keyboard
