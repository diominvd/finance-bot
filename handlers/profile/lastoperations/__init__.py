from config import dispatcher
from handlers.profile.lastoperations import command_handler
from handlers.profile.lastoperations import delete_last_operation_callback_handler


dispatcher.include_routers(
    command_handler.router,
    delete_last_operation_callback_handler.router
)