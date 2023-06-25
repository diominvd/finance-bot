from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import strings


def create_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=strings.keyboards['menu_keyboard']['add_operation'])
        ],
        [
            KeyboardButton(text=strings.keyboards['menu_keyboard']['last_operations'])
        ],
        [
            KeyboardButton(text=strings.keyboards['menu_keyboard']['profile']),
            KeyboardButton(text=strings.keyboards['menu_keyboard']['settings'])
        ]
    ]
    menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=keyboard_buttons)

    return menu_keyboard