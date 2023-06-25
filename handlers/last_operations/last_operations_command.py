from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.database import database_functions
from keyboards import delete_reply_keyboard, menu_kb, last_operations_kb
from states import LastOperationsStates
import strings

router = Router(name=__name__)

@router.message(Text('Последние операции'))
async def last_operations_command_handler(message: Message, state: FSMContext) -> None:
    # Fetch 5 last operations from database.
    last_operations: list = database_functions.select_last_operations_from_database(user_id=handlers.fetch_user_id(obj=message))

    if len(last_operations) == 0:
        await message.answer(text=strings.last_operations['last_operations_empty'],
                             reply_markup=menu_kb)
    else:
        # Remove menu reply keyboard.
        await delete_reply_keyboard(message=message)

        await message.answer(text=strings.last_operations['output_last_operations'](operations=last_operations),
                             reply_markup=last_operations_kb)

        # Set next state.
        await state.set_state(LastOperationsStates.get_callback)