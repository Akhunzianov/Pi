from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, ContentType, InlineKeyboardButton, InlineKeyboardMarkup

from handlers.states.state_user_registration import UserRegistrationStateGroup
from handlers.states.state_user_prefs_registration import UserPrefsRegistrationStateGroup
import utils.db_api.quick_commands as commands
from lexicon.lexicon_ru import lexicon, banned_words
import keyboards.layouts as keyboards
from keyboards.buttons_text import buttons_text


async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(lexicon['incorrect_int_format'], reply_markup=ReplyKeyboardRemove())
        return
    age = int(message.text)
    if age < 15:
        await message.answer(lexicon['low_age'], reply_markup=ReplyKeyboardRemove())
        return
    if age > 60:
        await message.answer(lexicon['high_age'], reply_markup=ReplyKeyboardRemove())
        return

    await state.update_data(age=age)
    await message.answer(lexicon['name'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserRegistrationStateGroup.wait_name)


async def process_name(message: Message, state: FSMContext):
    if any(banned_word in message.text.lower() for banned_word in banned_words):
        await message.answer(lexicon['data_security_error'])
        return

    if not message.text.isalpha():
        await message.answer(lexicon['incorrect_name_format'], reply_markup=ReplyKeyboardRemove())
        return

    await state.update_data(name=message.text)

    await message.answer(lexicon['gender'], reply_markup=keyboards.gender_choice_kb_inline)
    await state.set_state(UserRegistrationStateGroup.wait_gender)


async def process_gender_man(callback: CallbackQuery, state: FSMContext):
    await process_gender(callback, state, 'male')


async def process_gender_woman(callback: CallbackQuery, state: FSMContext):
    await process_gender(callback, state, 'female')


async def process_gender(callback: CallbackQuery, state: FSMContext, gender: str):
    await state.update_data(gender=gender)
    await callback.message.answer(lexicon['university'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserRegistrationStateGroup.wait_university)


async def process_university(message: Message, state: FSMContext):
    # TODO: Add check for university
    if any(banned_word in message.text.lower() for banned_word in banned_words):
        await message.answer(lexicon['data_security_error'])
        return

    await state.update_data(university=message.text)

    await message.answer(lexicon['degree'], reply_markup=keyboards.degree_kb_inline)
    await state.set_state(UserRegistrationStateGroup.wait_degree)


async def process_degree_bachelor(callback: CallbackQuery, state: FSMContext):
    await process_degree(callback, state, 'bachelor')


async def process_degree_master(callback: CallbackQuery, state: FSMContext):
    await process_degree(callback, state, 'master')


async def process_degree_post_graduate(callback: CallbackQuery, state: FSMContext):
    await process_degree(callback, state, 'post_graduate')


async def process_degree_graduated(callback: CallbackQuery, state: FSMContext):
    await state.update_data(degree='graduated', study_year=-1)
    await callback.message.answer(lexicon['major'])
    await state.set_state(UserRegistrationStateGroup.wait_major)


async def process_degree(callback: CallbackQuery, state: FSMContext, degree: str):
    await state.update_data(degree=degree)
    await callback.message.answer(lexicon['study_year'])
    await state.set_state(UserRegistrationStateGroup.wait_study_year)


async def process_study_year(message: Message, state: FSMContext):
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

    await state.update_data(study_year=study_year)
    await message.answer(lexicon['major'])
    await state.set_state(UserRegistrationStateGroup.wait_major)


async def process_major(message: Message, state: FSMContext):
    if any(banned_word in message.text.lower() for banned_word in banned_words):
        await message.answer(lexicon['data_security_error'])
        return

    await state.update_data(major=message.text)
    await message.answer(lexicon['media'])
    await state.set_state(UserRegistrationStateGroup.wait_media)


async def process_media(message: Message, state: FSMContext):
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
    await state.set_state(UserRegistrationStateGroup.wait_media_buttons)
    return


async def process_media_buttons_handler(message: Message, state: FSMContext):
    if message.text == buttons_text['add_media']:
        await message.answer(lexicon['media'], reply_markup=ReplyKeyboardRemove())
        await state.set_state(UserRegistrationStateGroup.wait_media)
        return
    if message.text == buttons_text['done_media']:
        await message.answer(lexicon['description'], reply_markup=ReplyKeyboardRemove())
        await state.set_state(UserRegistrationStateGroup.wait_description)
        return
    await message.answer(lexicon['no_such_button'])
    return


async def process_description(message: Message, state: FSMContext):
    if any(banned_word in message.text.lower() for banned_word in banned_words):
        await message.answer(lexicon['data_security_error'])
        return

    try:
        await state.update_data(description=message.text)
        await state.update_data(tg_username=message.from_user.username)
        user_data = await state.get_data()
        await commands.add_user(
            user_id=user_data['user_id'],
            name=user_data['name'],
            age=user_data['age'],
            gender=user_data['gender'],
            tg_username=user_data['tg_username'],
            university=user_data['university'],
            degree=user_data['degree'],
            study_year=user_data['study_year'],
            major=user_data['major'],
            description=user_data['description'],
            media=user_data['media'],
            media_tag=user_data['media_tag']
        )

        await message.answer(lexicon['preferred_gender_choice'], reply_markup=keyboards.gender_pref_kb_inline)
        await state.set_state(UserPrefsRegistrationStateGroup.wait_pref_gender)
    except Exception as e:
        await message.answer(lexicon['error_message'])
        await message.answer(lexicon['age'])
        await state.set_state(UserRegistrationStateGroup.wait_age)
