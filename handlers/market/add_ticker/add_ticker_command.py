from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards import add_ticker_kb
from states import MarketStates
import strings

router = Router(name=__name__)

@router.message(MarketStates.get_mode, Text('Добавить тикет'))
async def add_ticker_command_handler(message: Message, state: FSMContext):
    await message.answer(text=strings.market['add_ticker'],
                         reply_markup=add_ticker_kb)

    # Set state.
    await state.set_state(MarketStates.get_new_ticker)