from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import config
import database.load
import database.update
from keyboards import SettingsKeyboard
from keyboards.inline import categories_for_delete_keyboard
import lines
from states import EditIncomeCategories, EditExpenseCategories, SettingsStates
import utils as u

router = Router(name=__name__)


@router.callback_query(EditIncomeCategories.get_categories_for_delete, Text(startswith='category_'))
@router.callback_query(EditExpenseCategories.get_categories_for_delete, Text(startswith='category_'))
async def edit_deleted_categories__handler(callback: CallbackQuery, state: FSMContext, bot=config.bot) -> None:
    user_id: int = u.fetch_user_id(callback)
    chat_id: int = u.fetch_chat_id(callback)

    # Initializing categories dict.
    categories: dict = {}

    # Loading the appropriate categories for the user.
    match await state.get_state():
        case 'EditIncomeCategories:get_categories_for_delete':
            categories: dict = database.load.load_categories(user_id, 'income')
        case 'EditExpenseCategories:get_categories_for_delete':
            categories: dict = database.load.load_categories(user_id, 'expense')

    category: str = callback.data.split('_')[1]

    category_name: str = categories[category]['title']
    category_emoji: str = categories[category]['emoji']

    # Delete category from dict.
    categories.pop(category, None)

    match await state.get_state():
        case 'EditIncomeCategories:get_categories_for_delete':
            # Update categories in database.
            database.update.update_categories(user_id, 'income', categories)

            # Load updated categories.
            categories: dict = database.load.load_categories(user_id, 'income')
        case 'EditExpenseCategories:get_categories_for_delete':
            # Update categories in database.
            database.update.update_categories(user_id, 'expense', categories)

            # Load updated categories.
            categories: dict = database.load.load_categories(user_id, 'expense')

    # Check length of categories dict.
    if len(categories) == 0:
        # Send message about empty of categories list.
        await bot.edit_message_text(text=lines.edit_categories_lines['e-t-categories-empty'],
                                    chat_id=chat_id,
                                    message_id=u.fetch_message_id(callback),
                                    reply_markup=None)

        # Back to main menu.
        await bot.send_message(text=lines.other_lines['t-back-to-settings'],
                               chat_id=chat_id,
                               reply_markup=SettingsKeyboard)

        # Go to state -> SettingsStates.get_mode.
        await state.set_state(SettingsStates.get_mode)
    else:
        # Refresh inline keyboard with categories.
        await bot.edit_message_reply_markup(chat_id=chat_id,
                                            message_id=u.fetch_message_id(callback),
                                            reply_markup=categories_for_delete_keyboard.create_categories_for_delete_keyboard(categories))

        # Send message about deleted category.
        await bot.send_message(chat_id=chat_id,
                               text=lines.edit_categories_lines['d-t-category-deleted'](category_name, category_emoji))