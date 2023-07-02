from aiogram.fsm.state import StatesGroup, State


class StartStates(StatesGroup):
    get_currency = State()

class NewOperationStates(StatesGroup):
    get_category = State()
    get_value = State()

class LastOperationsStates(StatesGroup):
    get_callback = State()

class SettingsStates(StatesGroup):
    get_mode = State()
    get_ticker_for_delete = State()
    get_currency_for_change = State()