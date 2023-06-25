import aiogram.types
from config import dispatcher
import pydantic.main

from handlers.commands import start, help
dispatcher.include_routers(
    start.router,
    help.router
)

from handlers.new_operation import add_operation_command, operation_category
dispatcher.include_routers(
    add_operation_command.router,
    operation_category.router
)

from handlers.other import menu
dispatcher.include_routers(
    menu.router
)


def fetch_user_id(obj: pydantic.main.ModelMetaclass) -> int:
    return int(obj.from_user.id)


async def remove_callback_delay(callback_query: aiogram.types.CallbackQuery) -> None:
    await callback_query.answer(text=None,
                                show_alert=None)
    return None