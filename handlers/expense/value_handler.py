from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database.update
import lines
import storage
from keyboards import MenuKeyboard
from states import AddExpense
import utils as u


router = Router(name=__name__)


@router.message(AddExpense.set_expense_value)
async def expense_value_handler(message: Message, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(message)
    chat_id: int = u.fetch_chat_id(message)
    operation_currency: str = storage.bot_storage[user_id]['currency']

    try:
        # Try to transform message text to float value.
        operation_value: float = float(message.text)
    except ValueError:
        await message.answer(text=lines.new_operation_lines['e-t-incorrect-value'])
    else:
        if operation_value < 0:
            await message.answer(text=lines.new_operation_lines['e-t-incorrect-value'])
        else:
            # Update operation data in storage.
            storage.update_storage_data(user_id, 'value', operation_value)

            # Save operation into database.
            database.update.add_operation(user_id)

            # Edit message with value query,
            await bot.edit_message_text(text=lines.new_operation_lines['d-t-value-set'](operation_value, operation_currency),
                                        chat_id=chat_id,
                                        message_id=u.fetch_message_id(message) - 1)

            # Delete message with value from user.
            await bot.delete_message(chat_id=chat_id,
                                     message_id=u.fetch_message_id(message))

            # Send message about complete the operation.
            await message.answer(text=lines.new_operation_lines['d-t-operation-complete'](user_id),
                                 reply_markup=MenuKeyboard)

            # Remove operation from bot storage.
            storage.delete_operation(user_id)

            # Clear all states -> Return to menu.
            await state.clear()