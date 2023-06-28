from aiogram import Router, F
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
async def new_ticker_name_handler(message: Message):
    ticker_name: list = message.text.split('$')[1]

    # Formatting message text for answer.
    add_ticker_result_message_text: str = market_functions.add_new_ticker_for_user_in_database_market(user_id=handlers.fetch_user_id(obj=message),
                                                                                                      new_ticker_name=ticker_name)

    await message.answer(text=add_ticker_result_message_text,
                         reply_markup=add_ticker_kb)

@router.message(MarketStates.get_new_ticker, F.text != 'Отмена')
async def incorrect_new_ticker_name_handler(message: Message):
    await message.answer(text=strings.market['incorrect_ticker_name'])