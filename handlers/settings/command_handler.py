from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import lines
from keyboards import SettingsKeyboard
from states import SettingsStates


router = Router(name=__name__)


@router.message(Text(lines.keyboards_lines['menu-keyboard']['settings']))
async def settings_command_handler(message: Message, state: FSMContext) -> None:
    # Load user data from database.
    await message.answer(text=lines.other_lines['t-open-settings'],
                         reply_markup=SettingsKeyboard)

    # Set state -> ProfileStates.get_mode.
    await state.set_state(SettingsStates.get_mode)