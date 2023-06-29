from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards import market_kb
import lines
from states import MarketStates

router = Router(name=__name__)

@router.message(MarketStates.get_new_ticker, Text('Отмена'))
async def back_to_chapter_market_from_add_new_ticker(message: Message, state: FSMContext):
    await message.answer(text=lines.market_lines['text_back_to_market'],
                         reply_markup=market_kb)

    await state.set_state(MarketStates.get_mode)


@router.message(MarketStates.get_ticker_for_parsing, Text('Отмена'))
async def back_to_chapter_market_from_tickers_list(message: Message, state: FSMContext):
    await message.answer(text=lines.market_lines['text_back_to_market'],
                         reply_markup=market_kb)

    await state.set_state(MarketStates.get_mode)