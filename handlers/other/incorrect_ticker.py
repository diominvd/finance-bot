from aiogram import Router, F
from aiogram.types import Message

import lines
from states import MarketStates

router = Router(name=__name__)

"Handle incorrect message without $ symbol."
@router.message(MarketStates.get_new_ticker, F.text != 'Отмена')
async def incorrect_new_ticker_handler(message: Message):
    await message.answer(text=lines.market_lines['error_text_incorrect_ticker'])