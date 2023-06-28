from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.market import market_functions
from keyboards import add_ticker_kb
from states import MarketStates
import strings

router = Router(name=__name__)

@router.message(MarketStates.get_mode, Text('Добавить тикер'))
async def add_ticker_command_handler(message: Message, state: FSMContext):
    # Fetch user tickers from database and check limit.
    user_tickers: list = market_functions.select_all_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))
    print(len(user_tickers))
    if market_functions.check_user_tickers_limit(tickers_list=user_tickers):
        await message.answer(text=strings.market['max_tickers'])
    else:
        await message.answer(text=strings.market['add_ticker'],
                             reply_markup=add_ticker_kb)

        # Set state.
        await state.set_state(MarketStates.get_new_ticker)