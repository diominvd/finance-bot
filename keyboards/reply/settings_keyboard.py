from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import strings


def create_settings_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons = [
        [
            KeyboardButton(text=strings.keyboards['settings_keyboard']['clear_all_operations'])
        ],
        [
            KeyboardButton(text=strings.keyboards['settings_keyboard']['menu'])
        ]
    ]
    settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                            keyboard=keyboard_buttons)

    return settings_keyboard