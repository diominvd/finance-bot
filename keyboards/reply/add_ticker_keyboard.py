from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from strings import keyboards


def create_add_ticker_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards['add_ticker_keyboard']['cancel']),
        ]
    ]
    add_ticker_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                              keyboard=keyboard_buttons)

    return add_ticker_keyboard
