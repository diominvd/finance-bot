from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database.load
import lines
from keyboards import ProfileKeyboard
from states import ProfileStates
import utils as u


router = Router(name=__name__)


@router.message(Text(lines.keyboards_lines['menu-keyboard']['profile']))
async def profile_command_handler(message: Message, state: FSMContext) -> None:
    user_id: int = u.fetch_user_id(message)

    # Load user data from database.
    profile_info: tuple = database.load.load_profile_info(user_id)

    await message.answer(text=lines.profile_lines['d-t-profile-info'](profile_info),
                         reply_markup=ProfileKeyboard)

    # Set state -> ProfileStates.get_mode.
    await state.set_state(ProfileStates.get_mode)