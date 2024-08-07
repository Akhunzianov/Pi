from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputMediaPhoto, InputMediaVideo

from lexicon.lexicon_ru import lexicon
import utils.db_api.quick_commands as commands
from utils.tools.user_to_text import parse_user_to_text
from utils.tools.user_prefs_to_text import parse_user_preferences_to_text
import keyboards.layouts as keyboards
from handlers.states.general_states import GeneralStateGroup
from keyboards.buttons_text import buttons_text
from handlers.states.state_editing import EditingStateGroup


async def view_profile_setting(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = await commands.select_user(user_id)

    profile_text = parse_user_to_text(user)

    media = user.media
    media_tag = user.media_tag
    media_group = []
    flag = False
    for file_id, file_tag in zip(media, media_tag):
        if flag is False:
            if file_tag == 'photo':
                media_group.append(InputMediaPhoto(media=file_id, caption=profile_text))
            else:
                media_group.append(InputMediaVideo(media=file_id, caption=profile_text))
        else:
            if file_tag == 'photo':
                media_group.append(InputMediaPhoto(media=file_id))
            else:
                media_group.append(InputMediaVideo(media=file_id))
        flag = True

    await message.answer(lexicon['profile_message'], reply_markup=keyboards.my_profile_kb)
    await message.answer_media_group(media=media_group)
    await state.set_state(GeneralStateGroup.view_profile_button_handle)


async def view_profile_buttons_handler(message: Message, state: FSMContext):
    if message.text == buttons_text['edit_profile']:
        await message.answer(lexicon['edit_profile'], reply_markup=keyboards.edit_profile_kb)
        await state.set_state(EditingStateGroup.edit_profile_buttons_handle)
    elif message.text == buttons_text['preferences']:
        await view_preferences_setting(message, state)
    elif message.text == buttons_text['back']:
        await message.answer(text=lexicon['main_menu'], reply_markup=keyboards.main_menu_kb)
        await state.set_state(GeneralStateGroup.main_menu_button_handle)
        return
    else:
        await message.answer(lexicon['no_such_button'])
        return


async def view_preferences_setting(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_prefs = await commands.select_user_preferences(user_id)
    prefs_text = parse_user_preferences_to_text(user_prefs)

    await message.answer(text=prefs_text, reply_markup=keyboards.preferences_kb)
    await state.set_state(GeneralStateGroup.view_preferences_button_handle)
