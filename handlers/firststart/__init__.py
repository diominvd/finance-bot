from config import dispatcher
from handlers.firststart import balance_handler
from handlers.firststart import currency_handler
from handlers.firststart import expense_categories_handler
from handlers.firststart import income_categories_handler


dispatcher.include_routers(
    balance_handler.router,
    currency_handler.router,
    expense_categories_handler.router,
    income_categories_handler.router
)