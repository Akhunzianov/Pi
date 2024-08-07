from utils.db_api.shemas.user_preferences import UserPreferences


def parse_user_preferences_to_text(user_preferences: UserPreferences) -> str:
    string = 'Эти данные видны только тебе\n\n'
    if user_preferences.gender == 'female':
        gender = 'девушек'
    elif user_preferences.gender == 'male':
        gender = 'парней'
    else:
        gender = 'людей'
    string += f'Твои фильтры:\nТы ищешь {gender} в возрасте от {user_preferences.min_age} до {user_preferences.max_age} лет'
    return string