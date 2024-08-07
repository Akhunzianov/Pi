from utils.db_api.shemas.user import User


def parse_user_to_text(user: User) -> str:
    string = f'{user.name}, {user.age}, {user.university}\n'

    if user.degree == 'bachelor':
        string += 'Бакалавриат, '
    elif user.degree == 'master':
        string += 'Магистратура, '
    elif user.degree == 'post_graduate':
        string += 'Аспирантура, '

    if user.degree != 'graduated':
        string += f'{user.study_year} курс, '

    string += f'{user.major}\n\n'
    string += f'{user.description}'

    return string
