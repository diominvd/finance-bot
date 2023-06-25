import aiogram.types
from config import dispatcher
import pydantic.main

from handlers.commands import start, help
from handlers.new_operation import add_operation_command


dispatcher.include_routers(
    start.router,
    help.router
)
dispatcher.include_routers(
    add_operation_command.router
)


def fetch_user_id(obj: pydantic.main.ModelMetaclass) -> int:
    return int(obj.from_user.id)