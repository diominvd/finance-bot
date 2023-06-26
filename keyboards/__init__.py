from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import Message, ReplyKeyboardRemove

import config

from keyboards.reply import menu_keyboard, settings_keyboard
from keyboards.inline import categories_keyboard, last_operations_keyboard


menu_kb: ReplyKeyboardMarkup = menu_keyboard.create_menu_keyboard()
settings_kb: ReplyKeyboardMarkup = settings_keyboard.create_settings_keyboard()

categories_kb: InlineKeyboardMarkup = categories_keyboard.create_categories_keyboard()
last_operations_kb: InlineKeyboardMarkup = last_operations_keyboard.create_last_operations_keyboard()


async def delete_reply_keyboard(message: Message, bot=config.bot) -> None:
    await message.answer(text='Загрузка...',
                         reply_markup=ReplyKeyboardRemove())

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)