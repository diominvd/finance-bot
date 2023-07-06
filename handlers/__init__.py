from config import dispatcher
from handlers import commands
from handlers import firststart
from handlers import income
from handlers import expense
from handlers import profile
from handlers import lastoperations


dispatcher.include_routers(
    commands.router,
    firststart.router,
    income.router,
    expense.router,
    profile.router,
    lastoperations.router
)