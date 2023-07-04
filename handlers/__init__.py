from config import dispatcher
from handlers.commands import help, info, start


dispatcher.include_routers(
    start.router
)