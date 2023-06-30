from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data import market
import handlers
from keyboards.reply import user_tickers_keyboard, market_keyboard
import lines
from states import MarketStates

router = Router(name=__name__)

@router.message(MarketStates.get_ticker_for_delete, F.text != 'Отмена')
async def ticker_for_delete_handler(message: Message, state: FSMContext):
    # Fetch tickers list for check exists in user -> database.
    user_tickers: list = market.select_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    response_text: str = market.delete_user_ticker_from_database(user_id=handlers.fetch_user_id(obj=message), ticker=message.text)

    # Fetch refreshed user tickers list for keyboard.
    user_tickers: list = market.select_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    # If user have no tickers return to market menu.
    if len(user_tickers) == 0:
        await message.answer(text=lines.market_lines['text_ticker_deleted_tickers_list_empty'],
                             reply_markup=market_keyboard.create_market_keyboard(user_id=handlers.fetch_user_id(obj=message)))

        # Set state -> MarketStates.get_mode.
        await state.set_state(MarketStates.get_mode)
    else:
        await message.answer(text=lines.market_lines['text_ticker_deleted'],
                             reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))
