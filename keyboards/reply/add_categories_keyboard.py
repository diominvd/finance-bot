from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_add_categories_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['add-categories-keyboard']['cancel']),
        ]
    ]
    AddCategoriesKeyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                                     keyboard=keyboard_buttons)

    return AddCategoriesKeyboard
