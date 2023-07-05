from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database
from keyboards import menu_kb, currencies_kb
import lines
import utils as u
from states import FirstStart
import storage


router = Router(name=__name__)


@router.message(Command('start'))
async def command_start_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(message)

    if database.check_user(user_id):
        await message.answer(text=lines.commands_lines['command_text_start'],
                             reply_markup=menu_kb)
    else:
        # Add user id and username to bot storage.
        storage.bot_storage[user_id]: dict = {}
        storage.update_storage_data(user_id=u.fetch_user_id(message), key='user_id', value=u.fetch_user_id(message))
        storage.update_storage_data(user_id=u.fetch_user_id(message), key='username', value=u.fetch_user_username(message))

        await bot.send_message(chat_id=u.fetch_chat_id(message),
                               text=lines.first_start_lines['text_set_currency'],
                               reply_markup=currencies_kb)

        await state.set_state(FirstStart.set_currency)