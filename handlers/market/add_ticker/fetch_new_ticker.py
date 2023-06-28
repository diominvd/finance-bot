from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.market import market_functions
from keyboards import add_ticker_kb
from states import MarketStates
import strings

router = Router(name=__name__)


@router.message(MarketStates.get_new_ticker, Text(startswith='$'))
async def ticker_name_handler(message: Message, state: FSMContext):
    # Check correct ticker name (start with $).
    if message.text.startswith('$'):
        # Fetch ticker name from message.text.
        ticker_name: list = message.text.split('$')[1]

        # Check result of checking availability new ticker in user tickers:
        if market_functions.add_new_ticker_for_user_in_database_market(user_id=handlers.fetch_user_id(obj=message),
                                                                       new_ticker=ticker_name):
            await message.answer(text=strings.market['ticker_added'](ticker_name=ticker_name))
        else:
            await message.answer(text=strings.market['ticker_exists'])
    else:
        await message.answer(text=strings.market['incorrect_ticker_name'])