from aiogram.fsm.state import StatesGroup, State


class UsersInteractionStateGroup(StatesGroup):
    search_state = State()
    search_failed_buttons_handle = State()
    match_buttons_handle = State()
    likes_gallery_view_state = State()
    wait_show_likes_buttons = State()