from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['menu-keyboard']['income']),
            KeyboardButton(text=lines.keyboards_lines['menu-keyboard']['expense'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['menu-keyboard']['profile'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['menu-keyboard']['settings'])
        ]
    ]
    menu_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                       keyboard=keyboard_buttons)

    return menu_kb