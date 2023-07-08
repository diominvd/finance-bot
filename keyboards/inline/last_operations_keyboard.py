from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import lines


def create_last_operations_keyboard() -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [
            InlineKeyboardButton(text=lines.keyboards_lines['last-operations-keyboard']['delete_last']['title'],
                                 callback_data=lines.keyboards_lines['last-operations-keyboard']['delete_last']['callback_data'])
        ],
        [
            InlineKeyboardButton(text=lines.keyboards_lines['last-operations-keyboard']['cancel']['title'],
                                 callback_data=lines.keyboards_lines['last-operations-keyboard']['cancel']['callback_data'])
        ]
    ]
    LastOperationsKeyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return LastOperationsKeyboard