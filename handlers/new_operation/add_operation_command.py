from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data.storage import storage_functions
from keyboards import delete_reply_keyboard, categories_kb
from states import NewOperationStates
import strings

router = Router(name=__name__)

def date_formation() -> str:
    import datetime
    date: list = str(datetime.date.today()).split('-')
    date: str = f'{date[2]}.{date[1]}.{date[0]}'
    return date

@router.message(Text('Добавить операцию'))
async def add_operation_command_handler(message: Message, state: FSMContext) -> None:
    # Remove menu reply keyboard.
    await delete_reply_keyboard(message=message)

    # Create new operation in bot storage.
    storage_functions.insert_operation_into_bot_storage(obj=message)

    # Update operation date int bot storage.
    storage_functions.update_operation_data_in_bot_storage(obj=message,
                                                           field='date',
                                                           value=date_formation())

    await message.answer(text=strings.new_operation['choose_operation_category'],
                         reply_markup=categories_kb)

    # Set next state.
    await state.set_state(NewOperationStates.get_operation_category)
