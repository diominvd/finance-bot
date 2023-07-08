from config import dispatcher
from handlers.settings.editcategories import command_handler
from handlers.settings.editcategories import categories_type_handler
from handlers.settings.editcategories import mode_delete_handler
from handlers.settings.editcategories import deleted_categories_handler
from handlers.settings.editcategories import mode_add_handler
from handlers.settings.editcategories import new_categories_handler


dispatcher.include_routers(
    command_handler.router,
    categories_type_handler.router,
    mode_add_handler.router,
    mode_delete_handler.router,
    deleted_categories_handler.router,
    new_categories_handler.router
)