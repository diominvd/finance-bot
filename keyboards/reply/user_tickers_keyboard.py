from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import strings


def create_my_tickers_keyboard(tickers_list: list):
    keyboard_buttons: list = []

    if len(tickers_list) == 1:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0])
            ]
        ]
    elif len(tickers_list) == 2:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1])
            ]
        ]
    elif len(tickers_list) == 3:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1])
            ],
            [
                KeyboardButton(text=tickers_list[2])
            ]
        ]
    elif len(tickers_list) == 4:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1])
            ],
            [
                KeyboardButton(text=tickers_list[2]),
                KeyboardButton(text=tickers_list[3])
            ]
        ]
    elif len(tickers_list) == 5:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1]),
                KeyboardButton(text=tickers_list[2])
            ],
            [
                KeyboardButton(text=tickers_list[3]),
                KeyboardButton(text=tickers_list[4])
            ]
        ]
    elif len(tickers_list) == 6:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1]),
                KeyboardButton(text=tickers_list[2])
            ],
            [
                KeyboardButton(text=tickers_list[3]),
                KeyboardButton(text=tickers_list[4]),
                KeyboardButton(text=tickers_list[5])
            ]
        ]
    elif len(tickers_list) == 7:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1]),
                KeyboardButton(text=tickers_list[2])
            ],
            [
                KeyboardButton(text=tickers_list[3]),
                KeyboardButton(text=tickers_list[4]),
                KeyboardButton(text=tickers_list[5])
            ],
            [
                KeyboardButton(text=tickers_list[6])
            ]
        ]
    elif len(tickers_list) == 8:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1]),
                KeyboardButton(text=tickers_list[2])
            ],
            [
                KeyboardButton(text=tickers_list[3]),
                KeyboardButton(text=tickers_list[4]),
                KeyboardButton(text=tickers_list[5])
            ],
            [
                KeyboardButton(text=tickers_list[6]),
                KeyboardButton(text=tickers_list[7])
            ]
        ]
    elif len(tickers_list) == 9:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1]),
                KeyboardButton(text=tickers_list[2])
            ],
            [
                KeyboardButton(text=tickers_list[3]),
                KeyboardButton(text=tickers_list[4]),
                KeyboardButton(text=tickers_list[5])
            ],
            [
                KeyboardButton(text=tickers_list[6]),
                KeyboardButton(text=tickers_list[7]),
                KeyboardButton(text=tickers_list[8])
            ]
        ]
    elif len(tickers_list) == 10:
        keyboard_buttons = [
            [
                KeyboardButton(text=strings.keyboards['my_tickers_keyboard']['cancel'])
            ],
            [
                KeyboardButton(text=tickers_list[0]),
                KeyboardButton(text=tickers_list[1]),
                KeyboardButton(text=tickers_list[2])
            ],
            [
                KeyboardButton(text=tickers_list[3]),
                KeyboardButton(text=tickers_list[4]),
                KeyboardButton(text=tickers_list[5])
            ],
            [
                KeyboardButton(text=tickers_list[6]),
                KeyboardButton(text=tickers_list[7]),
                KeyboardButton(text=tickers_list[8])
            ],
            [
                KeyboardButton(text=tickers_list[9])
            ]
        ]
    my_ticker_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                             keyboard=keyboard_buttons)

    return my_ticker_keyboard