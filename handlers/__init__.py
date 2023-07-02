import aiogram.types
import pydantic.main

from config import dispatcher

from handlers import commands
from handlers import lastoperations


dispatcher.include_routers(
    commands.router,
    lastoperations.router
)

from handlers.new_operation import add_operation_command, operation_category, operation_value

dispatcher.include_routers(
    add_operation_command.router,
    operation_category.router,
    operation_value.router
)

from handlers.other import menu

dispatcher.include_routers(
    menu.router
)

from handlers.profile import profile_command_handler

dispatcher.include_routers(
    profile_command_handler.router
)

from handlers.settings import delete_all_operations, settings_command, change_currency_command

dispatcher.include_routers(
    delete_all_operations.router,
    settings_command.router,
    change_currency_command.router
)