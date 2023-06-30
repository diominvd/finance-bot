from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from config import bot
from data import database
import handlers
from keyboards import menu_kb, last_operations_kb
import lines
from states import LastOperationsStates

router = Router(name=__name__)

@router.callback_query(LastOperationsStates.get_callback, Text('delete_last'))
async def delete_last_operation_callback_handler(callback_query: CallbackQuery, state: FSMContext, bot=bot) -> None:
    # Remove callback delay.
    await handlers.remove_callback_delay(callback_query=callback_query)

    # Fetch 5 last operations from database.
    last_operations: list = database.delete_last_operation_from_database(user_id=handlers.fetch_user_id(obj=callback_query))

    # Check number of last operations.
    if len(last_operations) == 0:
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)

        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=lines.last_operations_lines['error_text_last_operations_empty'],
                               reply_markup=menu_kb)

        # Clear all states.
        await state.clear()
    else:
        await bot.edit_message_text(text=lines.last_operations_lines['def_text_last_operations'](user_id=handlers.fetch_user_id(obj=callback_query)),
                                    chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    reply_markup=last_operations_kb)