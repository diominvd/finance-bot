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

from handlers.profile import profile_command_handler
dispatcher.include_routers(
    profile_command_handler.router
)

from handlers.settings import settings_command_handler, delete_all_operations_handler
dispatcher.include_routers(
    settings_command_handler.router,
    delete_all_operations_handler.router
)

from handlers.other import menu
dispatcher.include_routers(
    menu.router
)


def date_formation() -> str:
    import datetime
    date: list = str(datetime.date.today()).split('-')
    date: str = f'{date[2]}.{date[1]}.{date[0]}'
    return date


def fetch_user_id(obj: pydantic.main.ModelMetaclass) -> int:
    return int(obj.from_user.id)

def fetch_user_username(obj: pydantic.main.ModelMetaclass) -> str:
    return str(obj.from_user.username)


async def remove_callback_delay(callback_query: aiogram.types.CallbackQuery) -> None:
    await callback_query.answer(text=None,
                                show_alert=None)
    return None