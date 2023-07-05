from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize


def create_categories_keyboard(categories: dict) -> InlineKeyboardMarkup:
    keyboard_buttons: list = []

    row = None
    for key, value in categories.items():
        title: str = value['title']
        emoji: str = emojize(value['emoji'])

        keyboard_buttons.append(InlineKeyboardButton(text=f'{emoji} | {title}', callback_data=f'category_{title}'))

    if len(keyboard_buttons) % 2 == 0:
        keyboard_buttons = [keyboard_buttons[i:i + 2] for i in range(0, len(keyboard_buttons), 2)]
    else:
        keyboard_buttons = [keyboard_buttons[i:i + 2] for i in range(0, len(keyboard_buttons) - 1, 2)] + [[keyboard_buttons[-1]]]

    keyboard_buttons.append([InlineKeyboardButton(text='Отмена', callback_data='cancel')])
    print(keyboard_buttons)

    categories_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return categories_keyboard

