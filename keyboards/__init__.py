from aiogram.types import Message, ReplyKeyboardRemove

import config

from keyboards.reply import menu_keyboard
from keyboards.inline import categories_keyboard


menu_kb = menu_keyboard.create_menu_keyboard()

categories_kb = categories_keyboard.create_categories_keyboard()


async def delete_reply_keyboard(message: Message, bot=config.bot) -> None:
    await message.answer(text='Загрузка...',
                         reply_markup=ReplyKeyboardRemove())

    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)