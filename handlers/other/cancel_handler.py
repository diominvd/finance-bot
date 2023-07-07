from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import lines
from keyboards import MenuKeyboard
from states import AddExpense, AddIncome, LastOperations
import utils as u


router = Router(name=__name__)


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


@router.message(Text('🏠 | Главное меню'))
async def main_menu_handler(message: Message, state: FSMContext, bot=config.bot):
    chat_id: int = u.fetch_chat_id(message)

    # Back to main menu.
    await bot.send_message(text=lines.other_lines['t-back-to-main-menu'],
                           chat_id=chat_id,
                           reply_markup=MenuKeyboard)

    # Clear all states.
    await state.clear()