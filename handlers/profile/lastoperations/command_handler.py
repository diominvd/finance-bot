from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database.load
import lines
from keyboards import ProfileKeyboard, LastOperationsKeyboard
from states import ProfileStates, LastOperations
import utils as u


router = Router(name=__name__)


@router.message(ProfileStates.get_mode, Text(lines.keyboards_lines['profile-keyboard']['last_operations']))
async def last_operations_command_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)

    # Load last user operations from database.
    last_operations: list = database.load.load_last_operations(user_id)

    # Checking that the user has operations.
    if len(last_operations) == 0:
        await bot.send_message(chat_id=u.fetch_chat_id(message),
                               text=lines.last_operations_lines['e-t-last-operations-empty'],
                               reply_markup=ProfileKeyboard)
    else:
        # Remove reply keyboard.
        await u.remove_reply_keyboard(message)

        # Send message with last operations + inline keyboard.
        await message.answer(text=lines.last_operations_lines['d-t-last-operations'](user_id, last_operations),
                             reply_markup=LastOperationsKeyboard)

        # Send message for get callback from inline keyboard.
        await state.set_state(LastOperations.get_callback)