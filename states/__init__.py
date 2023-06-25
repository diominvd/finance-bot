from aiogram.fsm.state import StatesGroup, State


class NewOperationStates(StatesGroup):
    get_operation_category = State()
    get_operation_value = State()