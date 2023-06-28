from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

import handlers
from data.database import database_functions
from keyboards import menu_kb
import strings

router = Router(name=__name__)

@router.message(Text('Биржа'))
async def market_command_handler(message: Message, state: FSMContext):
    pass