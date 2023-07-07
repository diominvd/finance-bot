from config import dispatcher
from handlers.lastoperations import command_handler
from handlers.lastoperations import delete_last_operation_callback_handler


dispatcher.include_routers(
    command_handler.router,
    delete_last_operation_callback_handler.router
)