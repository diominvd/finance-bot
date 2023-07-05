from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['menu_keyboard']['income']),
            KeyboardButton(text=lines.keyboards_lines['menu_keyboard']['expense'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['menu_keyboard']['profile'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['menu_keyboard']['settings'])
        ]
    ]
    kb_menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                       keyboard=keyboard_buttons)

    return kb_menu