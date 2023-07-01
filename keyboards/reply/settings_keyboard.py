from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lines import keyboards_lines


def create_settings_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards_lines['settings_keyboard']['clear_all_operations'])
        ],
        [
            KeyboardButton(text=keyboards_lines['settings_keyboard']['change_currency'])
        ],
        [
            KeyboardButton(text=keyboards_lines['settings_keyboard']['menu'])
        ]
    ]
    settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                            keyboard=keyboard_buttons)

    return settings_keyboard