from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from keyboards import settings_kb
import lines
from states import SettingsStates

router = Router(name=__name__)

@router.message(Text('Настройки'))
async def settings_command_handler(message: Message, state: FSMContext):
    await message.answer(text=lines.settings_lines['text_settings'],
                         reply_markup=settings_kb)

    # Set state -> SettingsStates.get_option.
    await state.set_state(SettingsStates.get_option)