from aiogram import Router, F
from aiogram.types import Message

from data import market
import handlers
from keyboards.reply import user_tickers_keyboard
import lines
from states import MarketStates

router = Router(name=__name__)

@router.message(MarketStates.get_ticker_for_parsing, F.text != 'Отмена')
async def ticker_for_parsing_handler(message: Message):
    # Fetch tickers list for creating tickers keyboard.
    user_tickers: list = market.select_user_tickers_from_database_market(user_id=handlers.fetch_user_id(obj=message))

    # Check ticker length.
    if not message.text.startswith('$'):
        await message.answer(text=lines.market_lines['error_text_incorrect_ticker'],
                             reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))
    else:
        # Check existence of ticker.
        if market.check_new_ticker_existence(ticker=message.text):
            # Check ticker in user tickers
            if message.text in user_tickers:
                await message.answer(text=lines.market_lines['def_text_ticker_value'](ticker=message.text),
                                     reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))
            else:
                await message.answer(text=lines.market_lines['error_text_ticker_not_added'],
                                     reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))
        else:
            await message.answer(text=lines.market_lines['error_text_incorrect_ticker'],
                                 reply_markup=user_tickers_keyboard.create_my_tickers_keyboard(tickers_list=user_tickers))