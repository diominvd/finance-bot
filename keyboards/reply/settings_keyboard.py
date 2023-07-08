from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_settings_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['settings-keyboard']['edit-categories'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['settings-keyboard']['main-menu'])
        ]
    ]
    SettingsKeyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                                keyboard=keyboard_buttons)

    return SettingsKeyboard
