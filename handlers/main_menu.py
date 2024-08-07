from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.buttons_text import buttons_text

from lexicon.lexicon_ru import lexicon
from handlers.user_profile.view_profile import view_profile_setting
from handlers.leave import leave
import keyboards.layouts as keyboards
from utils.db_api import quick_commands as commands
from handlers.users_interaction.search import search_setting


async def main_menu_button_handler(message: Message, state: FSMContext):
    await commands.edit_user_tg_username(message.from_user.id, message.from_user.username)
    if message.text == buttons_text['my_profile']:
        await view_profile_setting(message, state)
        return
    elif message.text == buttons_text['search']:
        await message.answer(lexicon['search'], reply_markup=keyboards.search_kb)
        await search_setting(message, state)
        return
    elif message.text == buttons_text['leave']:
        await leave(message, state)
        return
    await message.answer(lexicon['no_such_button'])
