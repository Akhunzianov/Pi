from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from lexicon.lexicon_ru import lexicon
import utils.db_api.quick_commands as commands
from handlers.states.state_user_registration import UserRegistrationStateGroup
from handlers.states.general_states import GeneralStateGroup
import keyboards.layouts as keyboards


async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(user_id=user_id)
    user = await commands.select_user(user_id)

    if not user:
        await message.answer(lexicon['start'], reply_markup=ReplyKeyboardRemove())
        await message.answer(lexicon['age'], reply_markup=ReplyKeyboardRemove())
        await state.set_state(UserRegistrationStateGroup.wait_age)
    else:
        await message.answer(lexicon['hey_again'], reply_markup=keyboards.main_menu_kb)
        await message.answer(text=lexicon['main_menu'])
        await state.set_state(GeneralStateGroup.main_menu_button_handle)




