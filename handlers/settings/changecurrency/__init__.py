from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import config
from data import database
import utils as u
from keyboards import settings_kb
from keyboards.inline import currencies_keyboard
from lines import keyboards_lines, currency_lines, settings_lines
from states import SettingsStates


router = Router(name=__name__)


"1. Handler: get command for change currency."
@router.message(SettingsStates.get_mode, Text(keyboards_lines['settings_keyboard']['change_currency']))
async def func_change_currency_h(message: Message, state: FSMContext) -> None:
    # Remove settings reply keyboard.
    await u.remove_reply_keyboard(message)
    
    # Send message with currencies keyboard.
    await message.answer(text=currency_lines['warning_text_change_currency'],
                         reply_markup=currencies_keyboard.create_currencies_keyboard(state=SettingsStates.get_mode))

    # Set state -> SettingsStates.get_currency_for_change.
    await state.set_state(SettingsStates.get_currency_for_change)


"1.1. Handler: get cancel callback an back to settings."
@router.callback_query(SettingsStates.get_currency_for_change, Text(startswith='cancel'))
@u.remove_callback_delay
async def func_change_currency_cancel_h(callback_query: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    # Remove inline keyboard with currencies.
    await bot.edit_message_reply_markup(chat_id=u.fetch_chat_id(callback_query),
                                        message_id=u.fetch_message_id(callback_query),
                                        reply_markup=None)

    # Back to settings.
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=settings_lines['text_settings'],
                           reply_markup=settings_kb)

    # Set state -> SettingsStates.get_mode.
    await state.set_state(SettingsStates.get_mode)


"1.2. Handler: get new currency from callback."
@router.callback_query(SettingsStates.get_currency_for_change, Text(startswith='currency_'))
@u.remove_callback_delay
async def func_new_currency_cb_h(callback_query: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    # Fetch currency from callback.
    new_currency: str = callback_query.data.split('_')[1]
    chat_id: int = u.fetch_chat_id(callback_query)

    database.delete_all_operations(user_id=u.fetch_user_id(callback_query))
    database.update_user_currency(user_id=u.fetch_user_id(callback_query), currency=new_currency)

    await bot.delete_message(chat_id=chat_id,
                             message_id=u.fetch_message_id(callback_query))

    # Send success message and back to settings.
    await bot.send_message(chat_id=chat_id,
                           text=currency_lines['text_currency_changed'](symbol=new_currency),
                           reply_markup=settings_kb)

    # Set state -> SettingsStates.get_option.
    await state.set_state(SettingsStates.get_mode)