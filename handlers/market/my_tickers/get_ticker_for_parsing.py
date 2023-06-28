from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.market import market_functions
from keyboards.reply import user_tickers_keyboard
from states import MarketStates
import strings

router = Router(name=__name__)

@router.message(MarketStates.get_ticker_for_parsing)
async def ticker_for_parsing_handler(message: Message, state: FSMContext, ):
    user_tickers: list = market_functions.select_all_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=strings.market['ticker_value_output'](ticker_name=message.text),
                         reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))