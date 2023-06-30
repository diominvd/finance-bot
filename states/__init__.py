from aiogram.fsm.state import StatesGroup, State

class NewOperationStates(StatesGroup):
    get_operation_category = State()
    get_operation_value = State()

class LastOperationsStates(StatesGroup):
    get_callback = State()

class MarketStates(StatesGroup):
    get_mode = State()
    get_new_ticker = State()
    get_ticker_for_parsing = State()
    get_ticker_for_delete = State()

class SettingsStates(StatesGroup):
    get_option = State()
    get_ticker_for_delete = State()