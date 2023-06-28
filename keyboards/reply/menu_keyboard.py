from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from strings import keyboards


def create_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards['menu_keyboard']['add_operation'])
        ],
        [
            KeyboardButton(text=keyboards['menu_keyboard']['last_operations'])
        ],
        [
            KeyboardButton(text=keyboards['menu_keyboard']['market']),
            KeyboardButton(text=keyboards['menu_keyboard']['profile'])
        ],
        [
            KeyboardButton(text=keyboards['menu_keyboard']['settings'])
        ]
    ]
    menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=keyboard_buttons)

    return menu_keyboard