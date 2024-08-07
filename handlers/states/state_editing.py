from aiogram.fsm.state import StatesGroup, State


class EditingStateGroup(StatesGroup):
    edit_profile_buttons_handle = State()
    wait_change_name = State()
    wait_change_age = State()
    wait_change_gender = State()
    wait_change_university = State()
    wait_change_degree = State()
    wait_change_study_year = State()
    wait_change_major = State()
    wait_change_media = State()
    wait_change_media_buttons = State()
    wait_change_description = State()

    wait_change_preferred_gender = State()
    wait_change_min_age = State()
    wait_change_max_age = State()