from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon
from keyboards.buttons_text import buttons_text
from handlers.user_profile.view_profile import view_profile_setting
import keyboards.layouts as keyboards
from handlers.states.state_editing import EditingStateGroup


async def view_preferences_buttons_handler(message: Message, state: FSMContext):
    if message.text == buttons_text['edit_preferences']:
        await message.answer(lexicon['change_preferred_gender'], reply_markup=keyboards.gender_pref_kb)
        await state.set_state(EditingStateGroup.wait_change_preferred_gender)
    elif message.text == buttons_text['back']:
        await view_profile_setting(message, state)
        return
    else:
        await message.answer(lexicon['no_such_button'])
