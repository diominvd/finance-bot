from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_edit_categories_mode_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['edit-categories-mode-keyboard']['add'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['edit-categories-mode-keyboard']['delete'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['edit-categories-mode-keyboard']['cancel'])
        ]
    ]
    EditCategoriesModeKeyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                                          keyboard=keyboard_buttons)

    return EditCategoriesModeKeyboard
