from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType, ReplyKeyboardRemove

from lexicon.lexicon_ru import lexicon
from keyboards.buttons_text import buttons_text
from handlers.user_profile.view_profile import view_profile_setting
from handlers.states.state_editing import EditingStateGroup
import keyboards.layouts as keyboards
import utils.db_api.quick_commands as commands


async def edit_profile_buttons_handler(message: Message, state: FSMContext):
    await commands.edit_user_tg_username(message.from_user.id, message.from_user.username)
    if message.text == buttons_text['all']:
        await message.answer(lexicon['change_name'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=False)
        await state.set_state(EditingStateGroup.wait_change_name)
        return
    elif message.text == buttons_text['name']:
        await message.answer(lexicon['change_name'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_name)
        return
    elif message.text == buttons_text['gender']:
        await message.answer(lexicon['change_gender'], reply_markup=keyboards.gender_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_gender)
        return
    elif message.text == buttons_text['age']:
        await message.answer(lexicon['change_age'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_age)
        return
    elif message.text == buttons_text['university']:
        await message.answer(lexicon['change_university'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_university)
        return
    elif message.text == buttons_text['degree']:
        await message.answer(lexicon['change_degree'], reply_markup=keyboards.degree_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_degree)
        return
    elif message.text == buttons_text['study_year']:
        await message.answer(lexicon['change_study_year'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_study_year)
        return
    elif message.text == buttons_text['major']:
        await message.answer(lexicon['change_major'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_major)
        return
    elif message.text == buttons_text['media']:
        await state.update_data(media=[], media_tag=[])
        await message.answer(lexicon['change_media'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_media)
        return
    elif message.text == buttons_text['description']:
        await message.answer(lexicon['change_description'], reply_markup=keyboards.leave_as_is_kb)
        await state.update_data(go_back=True)
        await state.set_state(EditingStateGroup.wait_change_description)
        return
    elif message.text == buttons_text['back']:
        await view_profile_setting(message, state)
        return
    elif message.text == buttons_text['easter']:
        await message.answer_sticker('CAACAgIAAxkBAAIOdmaxJvDENFT2Ae9JsBe6NLA2nt8xAAJ2NQACdtF4SUKLlXjGJ8cYNQQ')
        return
    await message.answer(lexicon['no_such_button'])


async def change_name(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text != buttons_text['leave_as_is']:
        if not message.text.isalpha():
            await message.answer(lexicon['incorrect_name_format'])
            return
        await commands.edit_user_name(message.from_user.id, message.text)

    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_age'])
        await state.set_state(EditingStateGroup.wait_change_age)


async def change_age(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text != buttons_text['leave_as_is']:
        if not message.text.isdigit():
            await message.answer(lexicon['incorrect_int_format'])
            return
        age = int(message.text)
        if age < 15:
            await message.answer(lexicon['low_age'])
            return
        if age > 60:
            await message.answer(lexicon['high_age'])
            return
        await commands.edit_user_age(message.from_user.id, age)

    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_gender'], reply_markup=keyboards.gender_kb)
        await state.set_state(EditingStateGroup.wait_change_gender)


async def change_gender(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text == buttons_text['male']:
        await commands.edit_user_gender(message.from_user.id, 'male')
    elif message.text == buttons_text['female']:
        await commands.edit_user_gender(message.from_user.id, 'female')
    else:
        await message.answer(lexicon['no_such_button'])
        return

    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_university'], reply_markup=keyboards.leave_as_is_kb)
        await state.set_state(EditingStateGroup.wait_change_university)


async def change_university(message: Message, state: FSMContext):
    # TODO: Add check for university
    data = await state.get_data()
    go_back = data['go_back']
    if message.text != buttons_text['leave_as_is']:
        await commands.edit_user_university(message.from_user.id, message.text)

    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_degree'], reply_markup=keyboards.degree_kb)
        await state.set_state(EditingStateGroup.wait_change_degree)


async def change_degree(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text == buttons_text['bachelor']:
        await commands.edit_user_degree(message.from_user.id, 'bachelor')
    elif message.text == buttons_text['master']:
        await commands.edit_user_degree(message.from_user.id, 'master')
    elif message.text == buttons_text['post_graduate']:
        await commands.edit_user_degree(message.from_user.id, 'post_graduate')
    elif message.text == buttons_text['graduated']:
        await commands.edit_user_degree(message.from_user.id, 'graduated')

        if go_back:
            await view_profile_setting(message, state)
            return
        else:
            await message.answer(lexicon['change_major'], reply_markup=keyboards.leave_as_is_kb)
            await state.set_state(EditingStateGroup.wait_change_major)
            return
    else:
        await message.answer(lexicon['no_such_button'])
        return

    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_study_year'], reply_markup=keyboards.leave_as_is_kb)
        await state.set_state(EditingStateGroup.wait_change_study_year)


async def change_study_year(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text != buttons_text['leave_as_is']:
        if not message.text.isdigit():
            await message.answer(lexicon['incorrect_int_format'])
            return
        study_year = int(message.text)
        if study_year < 1:
            await message.answer(lexicon['low_study_year'])
            return
        if study_year > 6:
            await message.answer(lexicon['high_study_year'])
            return
        await commands.edit_user_study_year(message.from_user.id, study_year)

    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_major'])
        await state.set_state(EditingStateGroup.wait_change_major)


async def change_major(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text != buttons_text['leave_as_is']:
        await commands.edit_user_major(message.from_user.id, message.text)

    if go_back:
        await view_profile_setting(message, state)
    else:
        await state.update_data(media=[], media_tag=[])
        await message.answer(lexicon['change_media'])
        await state.set_state(EditingStateGroup.wait_change_media)


async def change_media(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text != buttons_text['leave_as_is']:
        # TODO Add check for file size and number of files
        if message.content_type not in [ContentType.PHOTO, ContentType.VIDEO]:
            await message.answer(lexicon['media_error'])
            return
        data = await state.get_data()
        media = data.get('media', [])
        media_tag = data.get('media_tag', [])

        if message.content_type == ContentType.PHOTO:
            media.append(message.photo[-1].file_id)
            media_tag.append('photo')
        if message.content_type == ContentType.VIDEO:
            media.append(message.video.file_id)
            media_tag.append('video')
        await state.update_data(media=media)
        await state.update_data(media_tag=media_tag)

        await message.answer(lexicon['media_added'], reply_markup=keyboards.media_kb)
        await state.set_state(EditingStateGroup.wait_change_media_buttons)
        return
    if go_back:
        await view_profile_setting(message, state)
    else:
        await message.answer(lexicon['change_description'], reply_markup=keyboards.leave_as_is_kb)


async def change_media_buttons_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    go_back = data['go_back']
    if message.text == buttons_text['add_media']:
        await message.answer(lexicon['change_media'], reply_markup=ReplyKeyboardRemove())
        await state.set_state(EditingStateGroup.wait_change_media)
        return
    if message.text == buttons_text['done_media']:
        data = await state.get_data()
        media = data.get('media', [])
        media_tag = data.get('media_tag', [])
        await commands.edit_user_media(message.from_user.id, media, media_tag)
        await message.answer(lexicon['change_description'], reply_markup=keyboards.leave_as_is_kb)
        if go_back:
            await view_profile_setting(message, state)
            return
        else:
            await state.set_state(EditingStateGroup.wait_change_description)
            return
    await message.answer(lexicon['no_such_button'])


async def change_description(message: Message, state: FSMContext):
    if message.text != buttons_text['leave_as_is']:
        await commands.edit_user_description(message.from_user.id, message.text)
    await view_profile_setting(message, state)
