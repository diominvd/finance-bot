from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from data.storage import storage_functions
from keyboards import delete_reply_keyboard, categories_kb
from states import NewOperationStates
from strings import new_operation

router = Router(name=__name__)


@router.message(Text('Добавить операцию'))
async def add_operation_command_handler(message: Message, state: FSMContext):
	# Remove menu reply keyboard.
	await delete_reply_keyboard(message=message)

	# Create new operation in bot storage.
	storage_functions.insert_operation_into_bot_storage(obj=message)

	await message.answer(text=new_operation['choose_operation_category'],
	                     reply_markup=categories_kb)

	# Set next state.
	await state.set_state(NewOperationStates.get_operation_category)


