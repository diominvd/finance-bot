from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from strings import keyboards


def create_settings_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards['settings_keyboard']['clear_all_operations'])
        ],
        [
            KeyboardButton(text=keyboards['settings_keyboard']['menu'])
        ]
    ]
    settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                            keyboard=keyboard_buttons)

    return settings_keyboard