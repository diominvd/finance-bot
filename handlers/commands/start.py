from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data import database
import handlers
from keyboards import menu_kb
from keyboards.inline import currencies_keyboard
from lines import commands_lines, currency_lines
from states import ChooseCurrencyStates

router = Router(name=__name__)

@router.message(Command('start'))
async def start_command_handler(message: Message, state: FSMContext) -> None:
    if database.check_user_in_database(user_id=handlers.fetch_user_id(obj=message)):
        await message.answer(text=commands_lines['text_start_command'],
                             reply_markup=menu_kb)
    else:
        await message.answer(text=currency_lines['text_choose_currency'],
                             reply_markup=currencies_keyboard.create_currencies_keyboard())

        await state.set_state(ChooseCurrencyStates.get_currency)