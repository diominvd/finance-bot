from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_profile_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['profile_keyboard']['last_operations'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['profile_keyboard']['statistic'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['profile_keyboard']['main_menu'])
        ]
    ]
    profile_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=keyboard_buttons)

    return profile_kb
