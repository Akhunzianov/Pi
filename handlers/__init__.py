__all__ = ['start', 'register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart

from handlers.states.state_user_registration import UserRegistrationStateGroup
from handlers.states.state_user_prefs_registration import UserPrefsRegistrationStateGroup
from handlers.states.general_states import GeneralStateGroup
from handlers.states.state_editing import EditingStateGroup
from handlers.states.state_users_interaction import UsersInteractionStateGroup

from handlers.start import start
from handlers.leave import leave
from handlers.main_menu import main_menu_button_handler
from handlers.user_profile.view_profile import view_profile_buttons_handler
from handlers.user_profile.view_preferences import view_preferences_buttons_handler
from handlers.user_profile.edit_preferences import change_preferred_gender, change_max_age, change_min_age
from handlers.users_interaction.likes_gallery import likes_gallery_match_buttons_handler, show_likes_buttons_handler
from handlers.users_interaction.search import (
    process_search_buttons_handler,
    process_search_failed_buttons_handler,
    process_match_buttons_handler)
from handlers.user_registration.user_registration import (
    process_age,
    process_name,
    process_gender_man,
    process_gender_woman,
    process_university,
    process_degree_master,
    process_degree_bachelor,
    process_degree_post_graduate,
    process_degree_graduated,
    process_study_year,
    process_major,
    process_media,
    process_media_buttons_handler,
    process_description
)
from handlers.user_registration.user_prefs_registration import (
    process_pref_gender,
    process_pref_gender_man,
    process_pref_gender_woman,
    process_no_pref_gender,
    process_min_age_retry,
    process_pref_min_age,
    process_max_age_retry,
    process_pref_max_age
)
from handlers.user_profile.edit_profile import (
    change_name,
    change_age,
    change_gender,
    change_university,
    change_degree,
    change_study_year,
    change_major,
    change_media,
    change_media_buttons_handler,
    change_description,
    edit_profile_buttons_handler
)

def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(leave, F.data == 'leave')

    router.message.register(process_age, UserRegistrationStateGroup.wait_age)
    router.message.register(process_name, UserRegistrationStateGroup.wait_name)
    router.callback_query.register(process_gender_man, F.data == 'man_gender_picked')
    router.callback_query.register(process_gender_woman, F.data == 'woman_gender_picked')
    router.message.register(process_university, UserRegistrationStateGroup.wait_university)
    router.callback_query.register(process_degree_bachelor, F.data == 'bachelor_degree_picked')
    router.callback_query.register(process_degree_master, F.data == 'master_degree_picked')
    router.callback_query.register(process_degree_post_graduate, F.data == 'post_graduate_degree_picked')
    router.callback_query.register(process_degree_graduated, F.data == 'graduated_degree_picked')
    router.message.register(process_study_year, UserRegistrationStateGroup.wait_study_year)
    router.message.register(process_major, UserRegistrationStateGroup.wait_major)
    router.message.register(process_media, UserRegistrationStateGroup.wait_media)
    router.message.register(process_media_buttons_handler, UserRegistrationStateGroup.wait_media_buttons)
    router.message.register(process_description, UserRegistrationStateGroup.wait_description)

    router.callback_query.register(process_pref_gender_man, F.data == 'man_gender_preference')
    router.callback_query.register(process_pref_gender_woman, F.data == 'woman_gender_preference')
    router.callback_query.register(process_no_pref_gender, F.data == 'no_gender_preference')
    router.message.register(process_pref_min_age, UserPrefsRegistrationStateGroup.wait_min_age)
    router.callback_query.register(process_min_age_retry, F.data == 'min_age_retry')
    router.callback_query.register(process_max_age_retry, F.data == 'max_age_retry')
    router.message.register(process_pref_max_age, UserPrefsRegistrationStateGroup.wait_max_age)

    router.message.register(main_menu_button_handler, GeneralStateGroup.main_menu_button_handle)

    router.message.register(process_search_buttons_handler, UsersInteractionStateGroup.search_state)
    router.message.register(process_search_failed_buttons_handler, UsersInteractionStateGroup.search_failed_buttons_handle)
    router.message.register(process_match_buttons_handler, UsersInteractionStateGroup.match_buttons_handle)

    router.message.register(show_likes_buttons_handler, UsersInteractionStateGroup.wait_show_likes_buttons)
    router.message.register(likes_gallery_match_buttons_handler, UsersInteractionStateGroup.likes_gallery_view_state)

    router.message.register(view_profile_buttons_handler, GeneralStateGroup.view_profile_button_handle)
    router.message.register(edit_profile_buttons_handler, EditingStateGroup.edit_profile_buttons_handle)
    router.message.register(change_name, EditingStateGroup.wait_change_name)
    router.message.register(change_age, EditingStateGroup.wait_change_age)
    router.message.register(change_gender, EditingStateGroup.wait_change_gender)
    router.message.register(change_university, EditingStateGroup.wait_change_university)
    router.message.register(change_degree, EditingStateGroup.wait_change_degree)
    router.message.register(change_study_year, EditingStateGroup.wait_change_study_year)
    router.message.register(change_major, EditingStateGroup.wait_change_major)
    router.message.register(change_media, EditingStateGroup.wait_change_media)
    router.message.register(change_media_buttons_handler, EditingStateGroup.wait_change_media_buttons)
    router.message.register(change_description, EditingStateGroup.wait_change_description)

    router.message.register(view_preferences_buttons_handler, GeneralStateGroup.view_preferences_button_handle)
    router.message.register(change_preferred_gender, EditingStateGroup.wait_change_preferred_gender)
    router.message.register(change_min_age, EditingStateGroup.wait_change_min_age)
    router.message.register(change_max_age, EditingStateGroup.wait_change_max_age)
