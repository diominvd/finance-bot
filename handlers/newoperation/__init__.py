from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from config import bot
from data import database, storage
from handlers import utils as u
import keyboards
from keyboards import menu_kb, categories_kb
import lines
from lines import new_operation_lines
from states import LastOperationsStates, NewOperationStates


router = Router(name=__name__)
"""
    File Documentation:
        'func' in def names = function.
        'h' in def names = handler.
        'cb' in def names = callback.
"""


"1. Handler: handle command for add new operation."
@router.message(Text('Добавить операцию'))
async def func_add_operation_h(message: Message, state: FSMContext) -> None:
    # Remove menu reply keyboard.
    await keyboards.delete_reply_keyboard(message)

    # Create new operation in bot storage.
    storage.create_operation(user_id=u.fetch_user_id(message))

    # Update operation data (date) in bot storage.
    storage.update_operation_data(user_id=u.fetch_user_id(message),
                                  field='date',
                                  value=lines.current_date_formation())

    # Send message with categories keyboard.
    await message.answer(text=new_operation_lines['text_choose_category'],
                         reply_markup=categories_kb)

    # Set state -> NewOperationStates.get_category.
    await state.set_state(NewOperationStates.get_category)


"2. Handler: handle operation category from callback."
@router.callback_query(NewOperationStates.get_category, Text(startswith='category_'))
@u.remove_callback_delay
async def operation_category_handler(callback_query: CallbackQuery, state: FSMContext, bot=bot) -> None:
    # Fetch category from callback.
    operation_category: str = callback_query.data.split('_')[1]

    # Update operation data in bot storage.
    storage.update_operation_data(user_id=u.fetch_user_id(callback_query),
                                  field='category',
                                  value=operation_category)

    # Remove categories keyboard and change categories message text.
    await bot.edit_message_text(text=new_operation_lines['def_text_category_chosen'](category=operation_category),
                                chat_id=u.fetch_chat_id(callback_query),
                                message_id=u.fetch_message_id(callback_query),
                                reply_markup=None)

    # Send message to get operation value.
    await bot.send_message(chat_id=u.fetch_chat_id(callback_query),
                           text=new_operation_lines['text_input_value'])

    # Set next state.
    await state.set_state(NewOperationStates.get_value)


def check_value_format(message: Message) -> bool:
    try:
        value: float = float(message.text)
    except ValueError:
        return False
    else:
        if value <= 0:
            return False
        else:
            return True


"3. Handler: handle operation value from message."
@router.message(NewOperationStates.get_value)
async def operation_value_handler(message: Message, state: FSMContext, bot=bot) -> None:
    # Checking correct value of operation.
    if check_value_format(message):
        value: float = float(message.text)

        # Update operation data (value) int bot storage.
        storage.update_operation_data(user_id=u.fetch_user_id(message),
                                      field='value',
                                      value=value)

        # Insert operation data into database.
        database.add_operation(user_id=u.fetch_user_id(message))

        # Edi message with value query.
        await bot.edit_message_text(text=new_operation_lines['def_text_value_inputted'](user_id=u.fetch_user_id(message), value=value),
                                    chat_id=u.fetch_chat_id(message),
                                    message_id=u.fetch_message_id(message) - 1)

        # Delete message from user with value.
        await bot.delete_message(u.fetch_chat_id(message),
                                 message_id=u.fetch_message_id(message))

        # Send message with operation data.
        await bot.send_message(chat_id=u.fetch_chat_id(message),
                               text=new_operation_lines['def_text_operation_complete'](user_id=u.fetch_user_id(message)),
                               reply_markup=menu_kb)

        # Delete operation from bot storage.
        storage.remove_operation(user_id=u.fetch_user_id(message))

        # Clear all states = Back to main menu.
        await state.clear()
    else:
        await message.answer(text=new_operation_lines['error_text_incorrect_value'])