from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from handlers.states.general_states import GeneralStateGroup
from handlers.states.state_user_prefs_registration import UserPrefsRegistrationStateGroup
import utils.db_api.quick_commands as commands
from lexicon.lexicon_ru import lexicon
import keyboards.layouts as keyboards


async def process_pref_gender_man(callback: CallbackQuery, state: FSMContext):
    await process_pref_gender(callback, state, 'male')


async def process_pref_gender_woman(callback: CallbackQuery, state: FSMContext):
    await process_pref_gender(callback, state, 'female')


async def process_no_pref_gender(callback: CallbackQuery, state: FSMContext):
    await process_pref_gender(callback, state, 'no_pref')


async def process_pref_gender(callback: CallbackQuery, state: FSMContext, gender: str):
    await state.update_data(preferred_gender=gender)
    await callback.message.answer(lexicon['pref_min_age'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserPrefsRegistrationStateGroup.wait_min_age)


async def process_min_age_retry(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(lexicon['pref_min_age'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserPrefsRegistrationStateGroup.wait_min_age)


async def process_pref_min_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(lexicon['incorrect_int_format'])
        return
    age = int(message.text)
    if age < 15:
        await message.answer(lexicon['low_pref_age'], reply_markup=ReplyKeyboardRemove())
        return
    if age > 60:
        await message.answer(lexicon['high_pref_age'], reply_markup=ReplyKeyboardRemove())
        return

    await state.update_data(preferred_min_age=age)
    await message.answer(lexicon['pref_max_age'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserPrefsRegistrationStateGroup.wait_max_age)


async def process_max_age_retry(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(lexicon['pref_max_age'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserPrefsRegistrationStateGroup.wait_max_age)


async def process_pref_max_age(message: Message, state: FSMContext):
    try:
        if not message.text.isdigit():
            await message.answer(lexicon['incorrect_int_format'])
            return
        age = int(message.text)
        if age < 15:
            await message.answer(lexicon['low_pref_age'], reply_markup=ReplyKeyboardRemove())
            return
        if age > 60:
            await message.answer(lexicon['high_pref_age'], reply_markup=ReplyKeyboardRemove())
            return

        await state.update_data(preferred_max_age=age)
        user_prefs_data = await state.get_data()
        await commands.add_user_preferences(
            user_id=user_prefs_data['user_id'],
            gender=user_prefs_data['preferred_gender'],
            min_age=user_prefs_data['preferred_min_age'],
            max_age=user_prefs_data['preferred_max_age']
        )
        await message.answer(lexicon['user_preferences_registration_success'], reply_markup=ReplyKeyboardRemove())
        await message.answer(text=lexicon['main_menu'], reply_markup=keyboards.main_menu_kb)
        await state.set_state(GeneralStateGroup.main_menu_button_handle)
    except Exception as e:
        await message.answer(lexicon['error_message'], reply_markup=ReplyKeyboardRemove())

        await message.answer(lexicon['preferred_gender_choice'], reply_markup=keyboards.gender_pref_kb_inline)
        await state.set_state(UserPrefsRegistrationStateGroup.wait_pref_gender)

