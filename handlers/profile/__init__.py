from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database
from keyboards import profile_kb
import lines
from states import ProfileStates
import utils as u

router = Router(name=__name__)


@router.message(Text(lines.keyboards_lines['menu_keyboard']['profile']))
async def profile_command_handler(message: Message, state: FSMContext) -> None:
    # Load user data from database.
    user_info: tuple = database.load_profile_info(user_id=u.fetch_user_id(message))

    await message.answer(text=lines.profile_lines['profile_info'](user_info),
                         reply_markup=profile_kb)

    await state.set_state(ProfileStates.get_mode)