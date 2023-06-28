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

@router.message(Text('Мои тикеры'))
async def my_ticker_handler(message: Message, state: FSMContext):
    user_tickers: list = market_functions.select_all_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    if user_tickers[0] == '':
        user_tickers.pop(0)
    else:
        pass

    if len(user_tickers) == 0:
        await message.answer(text=strings.market['tickers_empty'])
    else:
        await message.answer(text=strings.market['load_user_tickers_message'],
                             reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))

        await state.set_state(MarketStates.get_ticker_for_parsing)