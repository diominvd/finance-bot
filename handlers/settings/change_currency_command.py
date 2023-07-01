from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import config
from data import database
import handlers
from keyboards import settings_kb
from keyboards.inline import currencies_keyboard
from lines import currency_lines, settings_lines
from states import SettingsStates

router = Router(name=__name__)


@router.message(SettingsStates.get_option, Text('Изменить валюту'))
async def change_currency_command_handler(message: Message, state: FSMContext):
    await message.answer(text=currency_lines['warning_text_change_currency'],
                         reply_markup=currencies_keyboard.create_currencies_keyboard(state=SettingsStates.get_option))

    # Set state -> SettingsStates.get_currency_for_change.
    await state.set_state(SettingsStates.get_currency_for_change)


@router.callback_query(SettingsStates.get_currency_for_change, Text(startswith='currency_'))
async def new_currency_handler(callback_query: CallbackQuery, state: FSMContext, bot=config.bot):
    # Remove callback delay.
    await handlers.remove_callback_delay(callback_query=callback_query)

    # Fetch currency from callback.
    new_currency: str = callback_query.data.split('_')[1]

    database.delete_all_user_operations_from_database(user_id=handlers.fetch_user_id(obj=callback_query))

    database.update_user_currency(user_id=handlers.fetch_user_id(obj=callback_query), currency=new_currency)

    chat_id = callback_query.message.chat.id

    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=currency_lines['text_currency_changed'](symbol=new_currency),
                           reply_markup=settings_kb)

    # Set state -> SettingsStates.get_option.
    await state.set_state(SettingsStates.get_option)


@router.callback_query(SettingsStates.get_currency_for_change, Text(startswith='cancel'))
async def change_currency_cancel_handler(callback_query: CallbackQuery, state: FSMContext, bot=config.bot):
    # Remove callback delay.
    await handlers.remove_callback_delay(callback_query=callback_query)

    # Remove inline keyboard with currencies.
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=None)

    # BAck to settings.
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=settings_lines['text_settings'],
                           reply_markup=settings_kb)

    # Set state -> SettingsStates.get_option.
    await state.set_state(SettingsStates.get_option)
