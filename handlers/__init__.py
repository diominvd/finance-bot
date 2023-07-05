from config import dispatcher
from handlers import commands
from handlers import firststart
from handlers import income


dispatcher.include_routers(
    commands.router,
    firststart.router,
    income.router
)