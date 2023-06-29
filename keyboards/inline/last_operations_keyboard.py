from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lines import keyboards_lines


def create_last_operations_keyboard() -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [
            InlineKeyboardButton(text=keyboards_lines['last_operations_keyboard']['delete_last_operation']['title'],
                                 callback_data=keyboards_lines['last_operations_keyboard']['delete_last_operation']['callback_data'])
        ],
        [
            InlineKeyboardButton(text=keyboards_lines['last_operations_keyboard']['menu']['title'],
                                 callback_data=keyboards_lines['last_operations_keyboard']['menu']['callback_data'])
        ],
    ]
    last_operations_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return last_operations_keyboard
