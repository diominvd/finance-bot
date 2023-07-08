from config import dispatcher
from handlers.expense import category_handler
from handlers.expense import command_handler
from handlers.expense import value_handler


dispatcher.include_routers(
    category_handler.router,
    command_handler.router,
    value_handler.router
)