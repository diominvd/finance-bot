from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from config import bot
from data import storage
import handlers
from states import NewOperationStates
import lines

router = Router(name=__name__)


@router.callback_query(NewOperationStates.get_operation_category, Text(startswith='category_'))
async def operation_category_handler(callback_query: CallbackQuery, state: FSMContext, bot=bot) -> None:
    # Remove callback delay.
    await handlers.remove_callback_delay(callback_query=callback_query)

    # Fetch category from callback.
    operation_category: str = callback_query.data.split('_')[1]

    # Update operation data in bot storage.
    storage.update_operation_data_in_bot_storage(user_id=handlers.fetch_user_id(obj=callback_query),
                                                 field='category',
                                                 value=operation_category)

    # Remove categories keyboard.
    await bot.edit_message_text(text=lines.new_operation_lines['def_text_category_chosen'](category=operation_category),
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=None)

    # Send message to get operation value.
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=lines.new_operation_lines['text_input_value'])

    # Set next state.
    await state.set_state(NewOperationStates.get_operation_value)
