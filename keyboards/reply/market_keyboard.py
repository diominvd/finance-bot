from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data import market
from lines import keyboards_lines


def create_market_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    user_tickers: list = market.select_user_tickers_from_database_market(user_id=user_id)

    keyboard_buttons = [
        [
            KeyboardButton(text=keyboards_lines['market_keyboard']['my_tickers'])
        ],
        [
            KeyboardButton(text=keyboards_lines['market_keyboard']['add_ticker'])
        ],
        [
            KeyboardButton(text=keyboards_lines['market_keyboard']['menu'])
        ]
    ]

    if len(user_tickers) != 0:
        keyboard_buttons[1].append(KeyboardButton(text=keyboards_lines['market_keyboard']['delete_ticker']))

    market_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=keyboard_buttons)

    return market_keyboard