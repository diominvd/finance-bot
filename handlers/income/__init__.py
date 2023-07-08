from config import dispatcher
from handlers.income import category_handler
from handlers.income import command_handler
from handlers.income import value_handler


dispatcher.include_routers(
    category_handler.router,
    command_handler.router,
    value_handler.router
)