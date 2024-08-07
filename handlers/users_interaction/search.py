from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputMediaPhoto, InputMediaVideo

from config.bot_config import dp
from config.bot_config import bot
from lexicon.lexicon_ru import lexicon
import utils.db_api.quick_commands as commands
from utils.tools.user_to_text import parse_user_to_text
import keyboards.layouts as keyboards
from handlers.states.general_states import GeneralStateGroup
from handlers.states.state_users_interaction import UsersInteractionStateGroup
from keyboards.buttons_text import buttons_text
from utils.tools.match_to_text import match_to_text
from utils.db_api.shemas.user import User


async def search_setting(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_prefs = await commands.select_user_preferences(user_id)
    search_result = await commands.get_search_result(user_id, user_prefs.min_age, user_prefs.max_age, user_prefs.gender)
    if search_result:
        search_text = parse_user_to_text(search_result)
        media = search_result.media
        media_tag = search_result.media_tag
        media_group = []
        flag = False
        for file_id, file_tag in zip(media, media_tag):
            if flag is False:
                if file_tag == 'photo':
                    media_group.append(InputMediaPhoto(media=file_id, caption=search_text))
                else:
                    media_group.append(InputMediaVideo(media=file_id, caption=search_text))
            else:
                if file_tag == 'photo':
                    media_group.append(InputMediaPhoto(media=file_id))
                else:
                    media_group.append(InputMediaVideo(media=file_id))
            flag = True

        await state.update_data(search_result_id=search_result.user_id)
        await message.answer_media_group(media_group)
        await state.set_state(UsersInteractionStateGroup.search_state)
        return
    else:
        await message.answer(lexicon['search_failed'], reply_markup=keyboards.menu_kb)
        await state.set_state(UsersInteractionStateGroup.search_failed_buttons_handle)


async def process_search_buttons_handler(message: Message, state: FSMContext):
    if message.text == buttons_text['like']:
        data = await state.get_data()
        is_match = await commands.select_like(data['search_result_id'], message.from_user.id)
        await commands.add_to_seen(message.from_user.id, data['search_result_id'])
        await commands.add_to_likes(message.from_user.id, data['search_result_id'])

        likee = await commands.select_user(data['search_result_id'])
        liker = await commands.select_user(message.from_user.id)
        likee_state = dp.fsm.resolve_context(bot=bot, chat_id=likee.user_id, user_id=likee.user_id)

        if is_match:
            match_text = match_to_text(liker)
            await send_match_profile(liker, likee)
            await bot.send_message(chat_id=likee.user_id, text=match_text, reply_markup=keyboards.after_match_kb)
            await likee_state.set_state(UsersInteractionStateGroup.match_buttons_handle)

            match_text = match_to_text(likee)
            await send_match_profile(likee, liker)
            await message.answer(text=match_text, reply_markup=keyboards.after_match_kb)
            await state.set_state(UsersInteractionStateGroup.match_buttons_handle)

            await commands.delete_match_likes(liker.user_id, likee.user_id)
            await commands.delete_match_likes(likee.user_id, liker.user_id)

            return

        await likee_state.update_data(new_likes=True)
        await search_setting(message, state)
        return

    if message.text == buttons_text['dislike']:
        data = await state.get_data()
        await commands.add_to_seen(message.from_user.id, data['search_result_id'])
        await search_setting(message, state)
        return
    elif message.text == buttons_text['exit']:
        await message.answer(text=lexicon['main_menu'], reply_markup=keyboards.main_menu_kb)
        await state.set_state(GeneralStateGroup.main_menu_button_handle)
        return
    await message.answer(lexicon['no_such_button'])


async def send_match_profile(match_user: User, recipient_user: User):
    profile_text = parse_user_to_text(match_user)
    media = match_user.media
    media_tag = match_user.media_tag
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

    await bot.send_media_group(chat_id=recipient_user.user_id, media=media_group)
    return


async def process_search_failed_buttons_handler(message: Message, state: FSMContext):
    if message.text == buttons_text['menu']:
        await message.answer(text=lexicon['main_menu'], reply_markup=keyboards.main_menu_kb)
        await state.set_state(GeneralStateGroup.main_menu_button_handle)
        return
    await message.answer(lexicon['no_such_button'])


async def process_match_buttons_handler(message: Message, state: FSMContext):
    if message.text == buttons_text['resume_search']:
        await message.answer(lexicon['search'], reply_markup=keyboards.search_kb)
        await search_setting(message, state)
        return
    if message.text == buttons_text['menu']:
        await message.answer(text=lexicon['main_menu'], reply_markup=keyboards.main_menu_kb)
        await state.set_state(GeneralStateGroup.main_menu_button_handle)
        return
    await message.answer(lexicon['no_such_button'])
