from aiogram.fsm.state import StatesGroup, State


class FirstStart(StatesGroup):
    set_currency = State()
    set_balance = State()
    set_income_categories = State()
    set_expense_categories = State()


class AddIncome(StatesGroup):
    set_income_category = State()
    set_income_value = State()


class AddExpense(StatesGroup):
    set_expense_category = State()
    set_expense_value = State()


class ProfileStates(StatesGroup):
    get_mode = State()


class LastOperations(StatesGroup):
    get_callback = State()


class SettingsStates(StatesGroup):
    get_mode = State()


class EditCategories(StatesGroup):
    choose_categories_type = State()


class EditIncomeCategories(StatesGroup):
    get_mode = State()
    get_categories_for_add = State()
    get_categories_for_delete = State()


class EditExpenseCategories(StatesGroup):
    get_mode = State()
    get_categories_for_add = State()
    get_categories_for_delete = State()