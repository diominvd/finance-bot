from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data import market
import handlers
from keyboards.reply import user_tickers_keyboard
import lines
from states import MarketStates

router = Router(name=__name__)

@router.message(MarketStates.get_mode, Text('Удалить тикер'))
async def delete_tickers_command_handler(message: Message, state: FSMContext):
    # Fetch all user tickers from database/market.
    user_tickers: list = market.select_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    # Second check numbers of tickers.
    if len(user_tickers) == 0:
        await message.answer(text=lines.market_lines['error_text_tickers_empty'])
    else:
        await message.answer(text=lines.market_lines['text_user_tickers_for_delete'],
                             reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))

    # Set state -> MarketStates.get_ticker_for_delete.
    await state.set_state(MarketStates.get_ticker_for_delete)