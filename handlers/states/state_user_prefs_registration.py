from aiogram.fsm.state import StatesGroup, State


class UserPrefsRegistrationStateGroup(StatesGroup):
    wait_pref_gender = State()
    wait_min_age = State()
    wait_max_age = State()
