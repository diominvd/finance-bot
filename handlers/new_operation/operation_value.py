from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import config
import handlers
from data import database, storage
from keyboards import menu_kb
from states import NewOperationStates
import lines

router = Router(name=__name__)


@router.message(NewOperationStates.get_operation_value)
async def operation_value_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    # Fetch operation value from message.
    try:
        operation_value: float = float(message.text)
    except:
        await message.answer(text=lines.new_operation_lines['error_text_incorrect_value'])
    else:
        if operation_value < 0:
            await message.answer(text=lines.new_operation_lines['error_text_incorrect_value'])
        else:
            # Update operation value int bot storage.
            storage.update_operation_data_in_bot_storage(user_id=handlers.fetch_user_id(obj=message),
                                                         field='value',
                                                         value=operation_value)

            # Insert operation data into database.
            database.insert_operation_into_database_operations(user_id=handlers.fetch_user_id(obj=message))

            # Edit message with value query.
            await bot.edit_message_text(text=lines.new_operation_lines['def_text_value_inputted'](value=message.text),
                                        chat_id=message.chat.id,
                                        message_id=message.message_id - 1)

            # Delete message from user with value.
            await bot.delete_message(chat_id=message.chat.id,
                                     message_id=message.message_id)

            # Send final message.
            await bot.send_message(chat_id=message.chat.id,
                                   text=lines.new_operation_lines['def_text_operation_complete'](
                                       user_id=handlers.fetch_user_id(obj=message)),
                                   reply_markup=menu_kb)

            # Remove operation from bot storage.
            storage.remove_operation_from_bot_storage(user_id=handlers.fetch_user_id(obj=message))

            # Clear all states.
            await state.clear()