from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from config import bot
from data import database
import utils as u
from keyboards import menu_kb
from keyboards.inline import currencies_keyboard
from lines import commands_lines, currency_lines
from states import StartStates

router = Router(name=__name__)
"""
    File Documentation:
        'cmnd' in def names = command.
        'h' in def names = handler.
"""


"2. Handler: handle command /start -> check presence of a user in database."
@router.message(Command('start'))
async def cmnd_start_h(message: Message, state: FSMContext) -> None:
    # Checking the presence of a user in the database.
    if database.user_existence_check(user_id=u.fetch_user_id(message)):
        # If True: Offer to choose a currency.
        await message.answer(text=commands_lines['text_start_command'],
                             reply_markup=menu_kb)
    else:
        # If False: Skip choose a currency.
        await message.answer(text=currency_lines['text_choose_currency'],
                             reply_markup=currencies_keyboard.create_currencies_keyboard())

        # Set state -> StartStates.get_currency.
        await state.set_state(StartStates.get_currency)


"1.1. Handler: if user not in database -> handle currency."
@u.remove_callback_delay
@router.callback_query(StartStates.get_currency, Text(startswith='currency_'))
async def currency_h(callback_query: CallbackQuery, state: FSMContext, bot=bot):
    # Extracting the currency selected by the user from callback_query.
    currency: str = callback_query.data.split('_')[1]
    chat_id: int = u.fetch_chat_id(callback_query)

    # Create user in database.
    database.create_user(user_id=u.fetch_user_id(callback_query),
                         currency=currency)

    # Deleting a currency selection message.
    await bot.delete_message(chat_id=chat_id,
                             message_id=u.fetch_message_id(callback_query))

    # Sending a message with the selected currency.
    await bot.send_message(chat_id=chat_id,
                           text=currency_lines['def_text_currency_chosen'](symbol=currency))

    # Sending start message with menu keyboard.
    await bot.send_message(chat_id=chat_id,
                           text=commands_lines['text_start_command'],
                           reply_markup=menu_kb)

    # Clear all states.
    await state.clear()


"2. Handler: handle command /help."
@router.message(Command('help'))
async def cmnd_help_h(message: Message) -> None:
    # Sending message with help.
    await message.answer(text=commands_lines['text_help_command'])


"3. Handler: handle command /info."
@router.message(Command('info'))
async def cmnd_info_h(message: Message) -> None:
    # Sending message with info.
    await message.answer(text=commands_lines['text_info_command'])
