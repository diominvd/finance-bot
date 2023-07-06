from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import config
import database
from keyboards import last_operations_kb, profile_kb
import lines
from states import ProfileStates, LastOperations
import utils as u

router = Router(name=__name__)


@router.message(ProfileStates.get_mode, Text(lines.keyboards_lines['profile_keyboard']['last_operations']))
async def profile_command_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    # Remove reply keyboard.
    await u.remove_reply_keyboard(message)

    # Fetch last user operations from database.
    last_operations: list = database.load_last_operations(user_id=u.fetch_user_id(message))

    if len(last_operations) == 0:
        await bot.send_message(chat_id=u.fetch_chat_id(message),
                               text=lines.last_operations_lines['error_text_last_operations_empty'],
                               reply_markup=profile_kb)
    else:
        await message.answer(text=lines.last_operations_lines['def_text_last_operations'](user_id=u.fetch_user_id(message), operations_list=last_operations),
                             reply_markup=last_operations_kb)

        await state.set_state(LastOperations.get_callback)


@router.callback_query(LastOperations.get_callback, Text('delete_last'))
@u.remove_callback_delay
async def delete_last_operation_handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    database.delete_last_operation(user_id=u.fetch_user_id(callback))

    # Fetch last user operations from database.
    last_operations: list = database.load_last_operations(user_id=u.fetch_user_id(callback))

    if len(last_operations) == 0:
        await bot.send_message(chat_id=u.fetch_chat_id(callback),
                               text=lines.last_operations_lines['error_text_last_operations_empty'],
                               reply_markup=profile_kb)

        await bot.delete_message(chat_id=u.fetch_chat_id(callback),
                                 message_id=u.fetch_message_id(callback))

        await state.set_state(ProfileStates.get_mode)
    else:
        await bot.edit_message_text(text=lines.last_operations_lines['def_text_last_operations'](user_id=u.fetch_user_id(callback), operations_list=last_operations),
                                    chat_id=u.fetch_chat_id(callback),
                                    message_id=u.fetch_message_id(callback),
                                    reply_markup=last_operations_kb)