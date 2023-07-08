from config import dispatcher
from handlers.settings.editcategories import categories_type_handler
from handlers.settings.editcategories import command_handler
from handlers.settings.editcategories.delete import deleted_categories_handler, mode_delete_handler
from handlers.settings.editcategories.add import mode_add_handler, new_categories_handler


dispatcher.include_routers(
    categories_type_handler.router,
    command_handler.router,
    deleted_categories_handler.router,
    mode_add_handler.router,
    mode_delete_handler.router,
    new_categories_handler.router
)