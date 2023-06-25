from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data.storage import storage_functions
from keyboards import categories_kb
from states import NewOperationStates
from strings import new_operation

router = Router(name=__name__)


@router.message(Text('Добавить операцию'))
async def add_operation_command_handler(message: Message, state: FSMContext):
	# Create new operation in bot storage.
	storage_functions.insert_operation_into_bot_ram(obj=message)

	await message.answer(text=new_operation['choose_operation_category'],
	                     reply_markup=categories_kb)

	# Set new state.
	await state.set_state(NewOperationStates.get_operation_category)


