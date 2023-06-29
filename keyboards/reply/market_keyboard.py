from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lines import keyboards_lines


def create_market_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards_lines['market_keyboard']['add_ticker']),
            KeyboardButton(text=keyboards_lines['market_keyboard']['my_tickers'])
        ],
        [
            KeyboardButton(text=keyboards_lines['market_keyboard']['menu'])
        ]
    ]
    market_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=keyboard_buttons)

    return market_keyboard