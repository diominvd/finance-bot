from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import lines


def create_currencies_keyboard() -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [
            InlineKeyboardButton(text=lines.keyboards_lines['currencies-keyboard']['RUB']['title'], callback_data=lines.keyboards_lines['currencies-keyboard']['RUB']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies-keyboard']['BYN']['title'], callback_data=lines.keyboards_lines['currencies-keyboard']['BYN']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies-keyboard']['UAH']['title'], callback_data=lines.keyboards_lines['currencies-keyboard']['UAH']['callback_data'])
        ],
        [
            InlineKeyboardButton(text=lines.keyboards_lines['currencies-keyboard']['KZT']['title'], callback_data=lines.keyboards_lines['currencies-keyboard']['RUB']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies-keyboard']['USD']['title'], callback_data=lines.keyboards_lines['currencies-keyboard']['BYN']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies-keyboard']['EUR']['title'], callback_data=lines.keyboards_lines['currencies-keyboard']['UAH']['callback_data'])
        ]
    ]
    CurrenciesKeyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return CurrenciesKeyboard