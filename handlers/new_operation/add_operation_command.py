from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data import storage
from keyboards import delete_reply_keyboard, categories_kb
from states import NewOperationStates
import lines

router = Router(name=__name__)


@router.message(Text('Добавить операцию'))
async def add_operation_command_handler(message: Message, state: FSMContext) -> None:
    # Remove menu reply keyboard.
    await delete_reply_keyboard(message=message)

    # Create new operation in bot storage.
    storage.insert_operation_into_bot_storage(user_id=handlers.fetch_user_id(obj=message))

    # Update operation date int bot storage.
    storage.update_operation_data_in_bot_storage(user_id=handlers.fetch_user_id(obj=message),
                                                 field='date',
                                                 value=lines.current_date_formation())

    await message.answer(text=lines.new_operation_lines['text_choose_category'],
                         reply_markup=categories_kb)

    # Set next state.
    await state.set_state(NewOperationStates.get_operation_category)
