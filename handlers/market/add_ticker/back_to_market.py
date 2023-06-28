from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards import market_kb
from states import MarketStates
import strings

router = Router(name=__name__)


@router.message(MarketStates.get_new_ticker, Text('Отмена'))
async def back_to_chapter_market(message: Message, state: FSMContext):
    await message.answer(text=strings.market['back_to_market'],
                         reply_markup=market_kb)

    await state.set_state(MarketStates.get_mode)