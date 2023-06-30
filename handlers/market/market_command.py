from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data import market
from keyboards.reply import market_keyboard
from states import MarketStates
import lines

router = Router(name=__name__)

@router.message(Text('Биржа'))
async def market_command_handler(message: Message, state: FSMContext):
    # Insert new user into database/market.
    market.insert_new_user_into_database_market(user_id=handlers.fetch_user_id(obj=message))

    await message.answer(text=lines.market_lines['text_market'],
                         reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))

    # Set next state.
    await state.set_state(MarketStates.get_mode)