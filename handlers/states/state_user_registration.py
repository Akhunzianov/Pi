from aiogram.fsm.state import StatesGroup, State


class UserRegistrationStateGroup(StatesGroup):
    wait_age = State()
    wait_name = State()
    wait_gender = State()
    wait_university = State()
    wait_degree = State()
    wait_study_year = State()
    wait_major = State()
    wait_media = State()
    wait_media_buttons = State()
    wait_description = State()
