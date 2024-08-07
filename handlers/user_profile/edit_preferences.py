from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType, ReplyKeyboardRemove

from lexicon.lexicon_ru import lexicon
from keyboards.buttons_text import buttons_text
from handlers.user_profile.view_profile import view_preferences_setting
from handlers.states.state_editing import EditingStateGroup
import keyboards.layouts as keyboards
import utils.db_api.quick_commands as commands


async def change_preferred_gender(message: Message, state: FSMContext):
    if message.text == buttons_text['man_pref']:
        await commands.edit_user_preferred_gender(message.from_user.id, 'male')
        await message.answer(text=lexicon['pref_min_age'], reply_markup=keyboards.leave_as_is_kb)
        await state.set_state(EditingStateGroup.wait_change_min_age)
        return
    elif message.text == buttons_text['woman_pref']:
        await commands.edit_user_preferred_gender(message.from_user.id, 'female')
        await message.answer(text=lexicon['pref_min_age'], reply_markup=keyboards.leave_as_is_kb)
        await state.set_state(EditingStateGroup.wait_change_min_age)
        return
    elif message.text == buttons_text['no_pref']:
        await commands.edit_user_preferred_gender(message.from_user.id, 'no_pref')
        await message.answer(text=lexicon['pref_min_age'], reply_markup=keyboards.leave_as_is_kb)
        await state.set_state(EditingStateGroup.wait_change_min_age)
        return
    await message.answer(lexicon['no_such_button'], reply_markup=keyboards.leave_as_is_kb)


async def change_min_age(message: Message, state: FSMContext):
    if message.text != buttons_text['leave_as_is']:
        if not message.text.isdigit():
            await message.answer(lexicon['incorrect_int_format'])
            return
        min_age = int(message.text)
        if min_age < 15:
            await message.answer(lexicon['low_age'])
            return
        if min_age > 60:
            await message.answer(lexicon['high_age'])
            return
        await commands.edit_user_preferred_min_age(message.from_user.id, min_age)
    await message.answer(text=lexicon['pref_max_age'], reply_markup=keyboards.leave_as_is_kb)
    await state.set_state(EditingStateGroup.wait_change_max_age)


async def change_max_age(message: Message, state: FSMContext):
    if message.text != buttons_text['leave_as_is']:
        if not message.text.isdigit():
            await message.answer(lexicon['incorrect_int_format'])
            return
        max_age = int(message.text)
        if max_age < 15:
            await message.answer(lexicon['low_age'])
            return
        if max_age > 60:
            await message.answer(lexicon['high_age'])
            return
        await commands.edit_user_preferred_max_age(message.from_user.id, max_age)
    await view_preferences_setting(message, state)



