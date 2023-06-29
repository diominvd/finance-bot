from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data import database
import handlers
from keyboards import delete_reply_keyboard, menu_kb, last_operations_kb
import lines
from states import LastOperationsStates

router = Router(name=__name__)

@router.message(Text('Последние операции'))
async def last_operations_command_handler(message: Message, state: FSMContext) -> None:
    # Fetch 5 last operations from database.
    last_operations: list = database.select_operations_from_database_operations(user_id=handlers.fetch_user_id(obj=message), limit=5)

    # Check number of last operations.
    if len(last_operations) == 0:
        await message.answer(text=lines.last_operations_lines['error_text_last_operations_empty'],
                             reply_markup=menu_kb)
    else:
        # Remove menu reply keyboard.
        await delete_reply_keyboard(message=message)

        await message.answer(text=lines.last_operations_lines['def_text_last_operations'](user_id=handlers.fetch_user_id(obj=message)),
                             reply_markup=last_operations_kb)

        # Set state -> LastOperationsStates.get_callback.
        await state.set_state(LastOperationsStates.get_callback)