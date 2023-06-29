from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Text

import handlers
from data import market
from keyboards import add_ticker_kb
from states import MarketStates
import lines

router = Router(name=__name__)


@router.message(MarketStates.get_new_ticker, Text(startswith='$'))
async def new_ticker_name_handler(message: Message):
    ticker_name: list = message.text.split('$')[1]

    # Formatting message text for answer.
    add_ticker_result_message_text: str = market.add_new_ticker_for_user_in_database_market(user_id=handlers.fetch_user_id(obj=message),
                                                                                            new_ticker=ticker_name)

    await message.answer(text=add_ticker_result_message_text,
                         reply_markup=add_ticker_kb)


@router.message(MarketStates.get_new_ticker, F.text != 'Отмена')
async def incorrect_new_ticker_name_handler(message: Message):
    await message.answer(text=lines.market_lines['error_text_incorrect_ticker'])
