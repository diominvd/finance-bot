from config import dispatcher
from handlers.profile import command_handler


dispatcher.include_routers(
    command_handler.router
)