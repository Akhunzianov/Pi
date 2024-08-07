from asyncpg import UniqueViolationError
from sqlalchemy import func, select, and_

from utils.db_api.db_gino import db

from utils.db_api.shemas.user import User
from utils.db_api.shemas.user_preferences import UserPreferences
from utils.db_api.shemas.seen import Seen
from utils.db_api.shemas.likes import Likes


async def add_user(user_id: int, name: str, gender: str, tg_username: str, age: int, university: str, degree: str,
                   study_year: int, major: str, description: str, media: list, media_tag: list):
    try:
        user = User(user_id=user_id, name=name, gender=gender, tg_username=tg_username, age=age, university=university,
                    degree=degree, study_year=study_year, major=major, description=description, media=media,
                    media_tag=media_tag)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def add_user_preferences(user_id: int, min_age: int, max_age: int, gender: str):
    try:
        user_preferences = UserPreferences(user_id=user_id, min_age=min_age, max_age=max_age, gender=gender)
        await user_preferences.create()
    except UniqueViolationError:
        print('Префернеции пользователя не добавлены')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def select_user_preferences(user_id):
    user_preferences = await UserPreferences.query.where(UserPreferences.user_id == user_id).gino.first()
    return user_preferences


async def edit_user_name(user_id: int, new_name: str):
    user = await select_user(user_id)
    if user:
        await user.update(name=new_name).apply()
    else:
        print('User not found')


async def edit_user_age(user_id: int, new_age: int):
    user = await select_user(user_id)
    if user:
        await user.update(age=new_age).apply()
    else:
        print('User not found')


async def edit_user_gender(user_id: int, new_gender: str):
    user = await select_user(user_id)
    if user:
        await user.update(gender=new_gender).apply()
    else:
        print('User not found')


async def edit_user_university(user_id: int, new_university: str):
    user = await select_user(user_id)
    if user:
        await user.update(university=new_university).apply()
    else:
        print('User not found')


async def edit_user_degree(user_id: int, new_degree: str):
    user = await select_user(user_id)
    if user:
        await user.update(degree=new_degree).apply()
    else:
        print('User not found')


async def edit_user_study_year(user_id: int, new_study_year: int):
    user = await select_user(user_id)
    if user:
        await user.update(study_year=new_study_year).apply()
    else:
        print('User not found')


async def edit_user_major(user_id: int, new_major: str):
    user = await select_user(user_id)
    if user:
        await user.update(major=new_major).apply()
    else:
        print('User not found')


async def edit_user_media(user_id: int, new_media: list, new_media_tag: list):
    user = await select_user(user_id)
    if user:
        await user.update(media=new_media, media_tag=new_media_tag).apply()
    else:
        print('User not found')


async def edit_user_description(user_id: int, new_description: str):
    user = await select_user(user_id)
    if user:
        await user.update(description=new_description).apply()
    else:
        print('User not found')


async def edit_user_tg_username(user_id: int, new_tg_username: str):
    user = await select_user(user_id)
    if user:
        await user.update(tg_username=new_tg_username).apply()
    else:
        print('User not found')


async def edit_user_preferred_gender(user_id: int, new_pref_gender: str):
    user_prefs = await select_user_preferences(user_id)
    if user_prefs:
        await user_prefs.update(gender=new_pref_gender).apply()
    else:
        print('User not found')


async def edit_user_preferred_min_age(user_id: int, new_min_age: int):
    user_prefs = await select_user_preferences(user_id)
    if user_prefs:
        await user_prefs.update(min_age=new_min_age).apply()
    else:
        print('User not found')


async def edit_user_preferred_max_age(user_id: int, new_max_age: int):
    user_prefs = await select_user_preferences(user_id)
    if user_prefs:
        await user_prefs.update(max_age=new_max_age).apply()
    else:
        print('User not found')


async def get_search_result(user_id: int, min_age: int, max_age: int, preferred_gender: str):
    subquery = select([Seen.viewed_id]).where(Seen.viewer_id == user_id)
    filters = [
        User.user_id != user_id,
        User.age >= min_age,
        User.age <= max_age,
        User.user_id.notin_(subquery),
    ]

    if preferred_gender != 'no_pref':
        filters.append(User.gender == preferred_gender)
    query = (
        select([User])
        .where(and_(*filters))
        .order_by(func.random())
        .limit(1)
    )
    result = await db.first(query)

    return result


async def add_to_seen(viewer_id: int, viewed_id: int):
    try:
        view = Seen(viewer_id=viewer_id, viewed_id=viewed_id)
        await view.create()
    except UniqueViolationError:
        print('Просмотр не добавлен')


async def add_to_likes(liker_id: int, likee_id: int):
    try:
        like = Likes(liker_id=liker_id, likee_id=likee_id)
        await like.create()
    except UniqueViolationError:
        print('Просмотр не добавлен')


async def select_user_gender(user_id: int):
    user = await select_user(user_id)
    return user.gender


async def select_like(liker_id: int, likee_id: int):
    like = await Likes.query.where(and_(Likes.liker_id == liker_id, Likes.likee_id == likee_id)).gino.first()
    return like


async def delete_match_likes(liker_id: int, likee_id: int):
    await Likes.delete.where(and_(Likes.liker_id == liker_id, Likes.likee_id == likee_id)).gino.status()


async def get_like_gallery_view_result(user_id: int, min_age: int, max_age: int, preferred_gender: str):
    subquery = select([Likes.liker_id]).where(Likes.likee_id == user_id)
    filters = [
        User.user_id != user_id,
        User.age >= min_age,
        User.age <= max_age,
        User.user_id.in_(subquery)
    ]

    if preferred_gender != 'no_pref':
        filters.append(User.gender == preferred_gender)
    query = (
        select([User])
        .where(and_(*filters))
        .order_by(func.random())
        .limit(1)
    )
    result = await db.first(query)

    return result


async def select_liked_users():
    query = select([User]).where(User.user_id.in_(select([Likes.likee_id])))
    result = await db.all(query)
    return result


async def user_liked_count(user_id: int):
    count_query = select([func.count()]).where(Likes.likee_id == user_id)
    count = await db.scalar(count_query)
    return count
