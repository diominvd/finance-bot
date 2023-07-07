from config import dispatcher
from handlers.settings import command_handler


dispatcher.include_routers(
    command_handler.router
)