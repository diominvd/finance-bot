from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import lines


def create_profile_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: list = [
        [
            KeyboardButton(text=lines.keyboards_lines['profile-keyboard']['last_operations'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['profile-keyboard']['statistic'])
        ],
        [
            KeyboardButton(text=lines.keyboards_lines['profile-keyboard']['main_menu'])
        ]
    ]
    ProfileKeyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=keyboard_buttons)

    return ProfileKeyboard
