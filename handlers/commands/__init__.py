from config import dispatcher
from handlers.commands import help_command
from handlers.commands import info_handler
from handlers.commands import start_command


dispatcher.include_routers(
    help_command.router,
    info_handler.router,
    start_command.router
)