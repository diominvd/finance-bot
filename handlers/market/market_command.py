from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.market import market_functions
from keyboards import market_kb
from states import MarketStates
import strings

router = Router(name=__name__)

@router.message(Text('Биржа'))
async def market_command_handler(message: Message, state: FSMContext):
    # Insert new user into database/market.
    market_functions.insert_new_user_into_database_market(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=strings.market['start_market_message'],
                         reply_markup=market_kb)

    # Set next state.
    await state.set_state(MarketStates.get_mode)