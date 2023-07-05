from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import lines


def create_currencies_keyboard() -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [
            InlineKeyboardButton(text=lines.keyboards_lines['currencies_keyboard']['RUB']['title'], callback_data=lines.keyboards_lines['currencies_keyboard']['RUB']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies_keyboard']['BYN']['title'], callback_data=lines.keyboards_lines['currencies_keyboard']['BYN']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies_keyboard']['UAH']['title'], callback_data=lines.keyboards_lines['currencies_keyboard']['UAH']['callback_data'])
        ],
        [
            InlineKeyboardButton(text=lines.keyboards_lines['currencies_keyboard']['KZT']['title'], callback_data=lines.keyboards_lines['currencies_keyboard']['RUB']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies_keyboard']['USD']['title'], callback_data=lines.keyboards_lines['currencies_keyboard']['BYN']['callback_data']),
            InlineKeyboardButton(text=lines.keyboards_lines['currencies_keyboard']['EUR']['title'], callback_data=lines.keyboards_lines['currencies_keyboard']['UAH']['callback_data'])
        ]
    ]
    kb_currencies: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return kb_currencies