from aiogram.fsm.state import StatesGroup, State


class FirstStart(StatesGroup):
    set_currency = State()
    set_balance = State()
    set_income_categories = State()
    set_expense_categories = State()


class AddIncome(StatesGroup):
    set_income_category = State()