from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.storage import storage_functions
from keyboards import delete_reply_keyboard, categories_kb
from states import NewOperationStates
import strings

router = Router(name=__name__)

@router.message(Text('Добавить операцию'))
async def add_operation_command_handler(message: Message, state: FSMContext) -> None:
    # Remove menu reply keyboard.
    await delete_reply_keyboard(message=message)

    # Create new operation in bot storage.
    storage_functions.insert_operation_into_bot_storage(user_id=handlers.fetch_user_id(obj=message))

    # Update operation date int bot storage.
    storage_functions.update_operation_data_in_bot_storage(user_id=handlers.fetch_user_id(obj=message),
                                                           field='date',
                                                           value=handlers.date_formation())

    await message.answer(text=strings.new_operation['choose_operation_category'],
                         reply_markup=categories_kb)

    # Set next state.
    await state.set_state(NewOperationStates.get_operation_category)
