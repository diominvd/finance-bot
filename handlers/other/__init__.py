from config import dispatcher
from handlers.other import cancel_handler


dispatcher.include_routers(
    cancel_handler.router
)