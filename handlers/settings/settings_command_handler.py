from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import config
from keyboards import settings_kb
from states import SettingsStates
import strings

router = Router(name=__name__)

@router.message(Text('Настройки'))
async def settings_command_handler(message: Message, state: FSMContext):
    await message.answer(text=strings.settings['settings_command_message'],
                         reply_markup=settings_kb)

    # Set next state.
    await state.set_state(SettingsStates.get_option)