from utils.db_api.shemas.user import User


def match_to_text(likee: User):
    if likee.gender == 'male':
        t = 'Его'
    else:
        t = 'Её'
    string = f"Поздравляю, нашлась взаимная симпатия!\nТы и {likee.name} (@{likee.tg_username}) нашли друг друга!!! 🎉🎉🎉\n\n"
    string += f"{t} анкету отправил тебе в предыдущем сообщении!\n\nПриятного общения! Не забудьте пригласить команду Pi на свадьбу 😉"
    return string
