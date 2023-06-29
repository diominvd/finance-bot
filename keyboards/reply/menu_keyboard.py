from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lines import keyboards_lines

def create_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards_lines['menu_keyboard']['add_operation'])
        ],
        [
            KeyboardButton(text=keyboards_lines['menu_keyboard']['last_operations'])
        ],
        [
            KeyboardButton(text=keyboards_lines['menu_keyboard']['market']),
            KeyboardButton(text=keyboards_lines['menu_keyboard']['profile'])
        ],
        [
            KeyboardButton(text=keyboards_lines['menu_keyboard']['settings'])
        ]
    ]
    menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=keyboard_buttons)

    return menu_keyboard