from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import lines
from keyboards import MenuKeyboard, ProfileKeyboard, SettingsKeyboard
from states import AddExpense, AddIncome, LastOperations, ProfileStates, SettingsStates, EditCategories, EditIncomeCategories, EditExpenseCategories
import utils as u

router = Router(name=__name__)


"Handler: backing to main menu."
@router.message(Text('🏠 | Главное меню'))
async def main_menu_handler(message: Message, state: FSMContext, bot=config.bot):
    chat_id: int = u.fetch_chat_id(message)

    # Back to main menu.
    await bot.send_message(text=lines.other_lines['t-back-to-main-menu'],
                           chat_id=chat_id,
                           reply_markup=MenuKeyboard)

    # Clear all states.
    await state.clear()


"Handler: backing to main menu."
@router.callback_query(AddExpense.set_expense_category, Text(startswith='cancel'))
@router.callback_query(AddIncome.set_income_category, Text(startswith='cancel'))
@router.callback_query(LastOperations.get_callback, Text(startswith='cancel'))
@u.remove_callback_delay
async def cancel_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot):
    chat_id: int = u.fetch_chat_id(callback)

    # Remove inline categories keyboard and cancel operation.
    await bot.edit_message_text(text=lines.new_operation_lines['e-r-operation-canceled'],
                                chat_id=chat_id,
                                message_id=u.fetch_message_id(callback),
                                reply_markup=None)

    # Back to main menu.
    await bot.send_message(text=lines.other_lines['t-back-to-main-menu'],
                           chat_id=chat_id,
                           reply_markup=MenuKeyboard)

    # Clear all states.
    await state.clear()


"Handler: backing to profile."
@router.callback_query(LastOperations.get_callback, Text(startswith='cancel'))
@u.remove_callback_delay
async def cancel_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot):
    chat_id: int = u.fetch_chat_id(callback)

    # Remove inline categories keyboard and cancel operation.
    await bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=u.fetch_message_id(callback),
                                        reply_markup=None)

    # Back to main menu.
    await bot.send_message(text=lines.other_lines['t-back-to-profile'],
                           chat_id=chat_id,
                           reply_markup=ProfileKeyboard)

    # Clear all states.
    await state.set_state(ProfileStates.get_mode)


"Handler: backing to settings."
@router.message(EditCategories.choose_categories_type, Text(lines.keyboards_lines['categories-type-keyboard']['cancel']))
@router.message(EditIncomeCategories.get_mode, Text(lines.keyboards_lines['edit-categories-mode-keyboard']['cancel']))
@router.message(EditExpenseCategories.get_mode, Text(lines.keyboards_lines['edit-categories-mode-keyboard']['cancel']))
@router.message(EditIncomeCategories.get_categories_for_add, Text(lines.keyboards_lines['add-categories-keyboard']['cancel']))
@router.message(EditExpenseCategories.get_categories_for_add, Text(lines.keyboards_lines['add-categories-keyboard']['cancel']))
async def back_to_settings_handler(message: Message, state: FSMContext, bot=config.bot):
    chat_id: int = u.fetch_chat_id(message)

    # Back to Settings.
    await bot.send_message(text=lines.other_lines['t-back-to-settings'],
                           chat_id=chat_id,
                           reply_markup=SettingsKeyboard)

    # Set state -> SettingsStates.get_mode.
    await state.set_state(SettingsStates.get_mode)


"Handler: backing to settings."
@router.callback_query(EditIncomeCategories.get_categories_for_delete, Text('cancel'))
@router.callback_query(EditExpenseCategories.get_categories_for_delete, Text('cancel'))
@u.remove_callback_delay
async def cancel_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot):
    chat_id: int = u.fetch_chat_id(callback)

    # Remove inline keyboard.
    await bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=u.fetch_message_id(callback),
                                        reply_markup=None)

    # Back to settings.
    await bot.send_message(text=lines.other_lines['t-back-to-settings'],
                           chat_id=chat_id,
                           reply_markup=SettingsKeyboard)

    # Clear all states.
    await state.set_state(SettingsStates.get_mode)