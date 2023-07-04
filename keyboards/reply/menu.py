from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lines.keyboards import menu_keyboard


def create_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=menu_keyboard['income']),
            KeyboardButton(text=menu_keyboard['expense'])
        ],
        [
            KeyboardButton(text=menu_keyboard['profile'])
        ],
        [
            KeyboardButton(text=menu_keyboard['settings'])
        ]
    ]
    kb_menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                       keyboard=keyboard_buttons)

    return kb_menu