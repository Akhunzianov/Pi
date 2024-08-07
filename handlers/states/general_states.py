from aiogram.fsm.state import StatesGroup, State


class GeneralStateGroup(StatesGroup):
    main_menu_button_handle = State()
    view_profile_setting_state = State()
    view_profile_button_handle = State()
    view_preferences_setting_state = State()
    view_preferences_button_handle = State()