from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import config
import database.update
import database.load
import lines
from keyboards import ProfileKeyboard, LastOperationsKeyboard
from states import ProfileStates, LastOperations
import utils as u


router = Router(name=__name__)


@router.callback_query(LastOperations.get_callback, Text('delete_last'))
@u.remove_callback_delay
async def delete_last_operation_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(callback)
    chat_id: int = u.fetch_chat_id(callback)

    # Delete last operation from database.
    database.update.delete_last_operation(user_id)

    # Fetch last user operations from database.
    last_operations: list = database.load.load_last_operations(user_id)

    # Checking that the user has operations.
    if len(last_operations) == 0:
        # Send error message.
        await bot.send_message(chat_id=chat_id,
                               text=lines.last_operations_lines['e-t-last-operations-empty'],
                               reply_markup=ProfileKeyboard)

        # Delete message with last operations and inline keyboard.
        await bot.delete_message(chat_id=chat_id,
                                 message_id=u.fetch_message_id(callback))

        # Set state -> ProfileStates.get_mode.
        await state.set_state(ProfileStates.get_mode)
    else:
        # Send message with refreshed last operations list.
        await bot.edit_message_text(text=lines.last_operations_lines['d-t-last-operations'](user_id, last_operations),
                                    chat_id=chat_id,
                                    message_id=u.fetch_message_id(callback),
                                    reply_markup=LastOperationsKeyboard)