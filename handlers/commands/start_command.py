from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database.check
import database
import lines
import storage
from keyboards import MenuKeyboard, CurrenciesKeyboard
from states import FirstStart
import utils as u


router = Router(name=__name__)


@router.message(Command('start'))
async def command_start_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    # Extracting the user ID from message and check its presence in the database.
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)

    if database.check.check_user(user_id):
        await message.answer(text=lines.commands_lines['c-t-start'],
                             reply_markup=MenuKeyboard)
    else:
        # Add user id and username to bot storage.
        storage.registration(message)

        # Send message witch inline currencies keyboard.
        await bot.send_message(chat_id=chat_id,
                               text=lines.first_start_lines['t-choose-currency'],
                               reply_markup=CurrenciesKeyboard)

        # Set state FirstStart.set_currency.
        await state.set_state(FirstStart.set_currency)