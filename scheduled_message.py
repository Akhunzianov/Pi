import asyncio

from utils.db_api import quick_commands as commands
from config.bot_config import bot, dp
import keyboards.layouts as keyboards
from handlers.states.state_users_interaction import UsersInteractionStateGroup


gender_multi_dict = {'male': 'парням', 'female': 'девушкам', 'no_pref': 'людям'}
gender_single_dict = {'male': 'парню', 'female': 'девушке', 'no_pref': 'человеку'}
liked_dict = {'male': 'понравился', 'female': 'понравилась'}


async def send_scheduled_message():
    print("Performing scheduled message send")

    users = await commands.select_liked_users()
    for user in users:
        user_prefs = await commands.select_user_preferences(user.user_id)
        likes_count = await commands.user_liked_count(user.user_id)
        if likes_count % 10 == 1 and likes_count % 100 != 11:
            gender_dict = gender_single_dict
        else:
            gender_dict = gender_multi_dict
        text = f'Ты {liked_dict[user.gender]} {likes_count} {gender_dict[user_prefs.gender]}! Показать их?'

        state = dp.fsm.resolve_context(bot=bot, chat_id=user.user_id, user_id=user.user_id)
        data = await state.get_data()
        new_likes = data.get('new_likes', False)
        if new_likes:
            await bot.send_message(chat_id=user.user_id, text=text, reply_markup=keyboards.show_likes_kb)
            await state.set_state(UsersInteractionStateGroup.wait_show_likes_buttons)


async def scheduler():
    while True:
        await send_scheduled_message()
        await asyncio.sleep(3600)