from config import dispatcher

from handlers.commands import start, help


dispatcher.include_routers(
    start.router,
    help.router
)