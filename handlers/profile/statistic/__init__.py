from config import dispatcher
from handlers.profile.statistic import command_handler


dispatcher.include_routers(
    command_handler.router
)