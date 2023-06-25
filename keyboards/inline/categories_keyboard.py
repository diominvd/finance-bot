from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from strings import keyboards


def create_categories_keyboard() -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['products']['title'],
                                 callback_data=keyboards['categories_keyboard']['products']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['cafes']['title'],
                                 callback_data=keyboards['categories_keyboard']['cafes']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['auto']['title'],
                                 callback_data=keyboards['categories_keyboard']['auto']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['transport']['title'],
                                 callback_data=keyboards['categories_keyboard']['transport']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['home']['title'],
                                 callback_data=keyboards['categories_keyboard']['home']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['entertainment']['title'],
                                 callback_data=keyboards['categories_keyboard']['entertainment']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['sport']['title'],
                                 callback_data=keyboards['categories_keyboard']['sport']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['health']['title'],
                                 callback_data=keyboards['categories_keyboard']['health']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['education']['title'],
                                 callback_data=keyboards['categories_keyboard']['education']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['gifts']['title'],
                                 callback_data=keyboards['categories_keyboard']['gifts']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['beauty']['title'],
                                 callback_data=keyboards['categories_keyboard']['beauty']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['clothes']['title'],
                                 callback_data=keyboards['categories_keyboard']['clothes']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['technic']['title'],
                                 callback_data=keyboards['categories_keyboard']['technic']['callback_data']),
            InlineKeyboardButton(text=keyboards['categories_keyboard']['subscriptions']['title'],
                                 callback_data=keyboards['categories_keyboard']['subscriptions']['callback_data']),
        ],
        [
            InlineKeyboardButton(text=keyboards['categories_keyboard']['menu']['title'],
                                 callback_data=keyboards['categories_keyboard']['menu']['callback_data'])
        ]
    ]
    categories_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

    return categories_keyboard
