from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data import market
from keyboards import add_ticker_kb
from states import MarketStates
import lines

router = Router(name=__name__)

@router.message(MarketStates.get_mode, Text('Добавить тикер'))
async def add_ticker_text_command_handler(message: Message, state: FSMContext):
    # Fetch user tickers from database.
    user_tickers: list = market.select_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    # Check limit of tickers for user.
    if market.check_user_tickers_limit(tickers_list=user_tickers):
        await message.answer(text=lines.market_lines['error_text_tickers_limit'])
    else:
        await message.answer(text=lines.market_lines['text_add_ticker'],
                             reply_markup=add_ticker_kb)

        # Set state -> MarketStates.get_new_ticker.
        await state.set_state(MarketStates.get_new_ticker)