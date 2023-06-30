from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import Message, ReplyKeyboardRemove

import config

from keyboards.inline import categories_keyboard, last_operations_keyboard
from keyboards.reply import menu_keyboard, settings_keyboard, market_keyboard, add_ticker_keyboard, user_tickers_keyboard


categories_kb: InlineKeyboardMarkup = categories_keyboard.create_categories_keyboard()
last_operations_kb: InlineKeyboardMarkup = last_operations_keyboard.create_last_operations_keyboard()

menu_kb: ReplyKeyboardMarkup = menu_keyboard.create_menu_keyboard()
# market_kb: Dynamic keyboard. For use import def in file.
add_ticker_kb: ReplyKeyboardMarkup = add_ticker_keyboard.create_add_ticker_keyboard()
settings_kb: ReplyKeyboardMarkup = settings_keyboard.create_settings_keyboard()


async def delete_reply_keyboard(message: Message, bot=config.bot) -> None:
    await message.answer(text='Загрузка...',
                         reply_markup=ReplyKeyboardRemove())

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)