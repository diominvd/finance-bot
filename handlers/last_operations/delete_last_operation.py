from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from config import bot
from data.database import database_functions
from keyboards import menu_kb, last_operations_kb
import handlers
from states import LastOperationsStates
import strings

router = Router(name=__name__)

@router.callback_query(LastOperationsStates.get_callback, Text('delete_last'))
async def delete_last_operation_callback_handler(callback_query: CallbackQuery, state: FSMContext, bot=bot) -> None:
    # Remove callback delay.
    await handlers.remove_callback_delay(callback_query=callback_query)

    # Fetch 5 last operations from database.
    last_operations: list = database_functions.delete_last_operation_from_database(user_id=handlers.fetch_user_id(obj=callback_query))

    if len(last_operations) == 0:
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)

        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=strings.last_operations['last_operations_empty'],
                               reply_markup=menu_kb)

        # Clear all states.
        await state.clear()

    else:
        await bot.edit_message_text(text=strings.last_operations['output_last_operations'](operations=last_operations),
                                    chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    reply_markup=last_operations_kb)