from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from strings import keyboards


def create_market_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards['market_keyboard']['add_ticket'])
        ],
        [
            KeyboardButton(text=keyboards['market_keyboard']['my_tickets'])
        ],
        [
            KeyboardButton(text=keyboards['market_keyboard']['menu'])
        ]
    ]
    market_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=keyboard_buttons)

    return market_keyboard