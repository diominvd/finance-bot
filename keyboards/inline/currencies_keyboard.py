from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State

from lines import keyboards_lines
from states import SettingsStates


def create_currencies_keyboard(state: State = None) -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['RUB']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['RUB']['callback_data']),
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['BYN']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['BYN']['callback_data']),
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['UAH']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['UAH']['callback_data'])
        ],
        [
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['KZT']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['KZT']['callback_data']),
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['USD']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['USD']['callback_data']),
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['EUR']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['EUR']['callback_data'])
        ],
    ]

    if state == SettingsStates.get_option:
        keyboard_buttons.append([
            InlineKeyboardButton(text=keyboards_lines['currencies_keyboard']['cancel']['title'],
                                 callback_data=keyboards_lines['currencies_keyboard']['cancel']['callback_data'])
        ])
    currencies_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return currencies_keyboard