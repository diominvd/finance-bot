from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_categories_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['categories-type-keyboard']['income']),
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['categories-type-keyboard']['expense'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['categories-type-keyboard']['cancel'])
        ]
    ]
    CategoriesTypeKeyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                                      keyboard=keyboard_buttons)

    return CategoriesTypeKeyboard
