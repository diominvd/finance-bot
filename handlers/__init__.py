import aiogram.types
from config import dispatcher
import pydantic.main

from handlers.commands import start, help
dispatcher.include_routers(
    start.router,
    help.router
)

from handlers.new_operation import add_operation_command, operation_category, operation_value
dispatcher.include_routers(
    add_operation_command.router,
    operation_category.router,
    operation_value.router
)

from handlers.last_operations import last_operations_command, delete_last_operation
dispatcher.include_routers(
    last_operations_command.router,
    delete_last_operation.router
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