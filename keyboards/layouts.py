from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.buttons_text import buttons_text

start_button = KeyboardButton(text=buttons_text['start'])

start_kb = ReplyKeyboardMarkup(keyboard=[[start_button]], resize_keyboard=True)

search_button = KeyboardButton(text=buttons_text['search'])
view_my_profile_button = KeyboardButton(text=buttons_text['my_profile'])
edit_profile_button = KeyboardButton(text=buttons_text['edit_profile'])
leave_button = KeyboardButton(text=buttons_text['leave'])
leave_button_inline = InlineKeyboardButton(text=buttons_text['leave'], callback_data='leave')
back_button = KeyboardButton(text=buttons_text['back'])
preferences_button = KeyboardButton(text=buttons_text['preferences'])


main_menu_kb = ReplyKeyboardMarkup(keyboard=[[search_button, view_my_profile_button, leave_button]],
                                   resize_keyboard=True)
my_profile_kb = ReplyKeyboardMarkup(keyboard=[[edit_profile_button, preferences_button, back_button]],
                                    resize_keyboard=True)


like_button = KeyboardButton(text=buttons_text['like'])
dislike_button = KeyboardButton(text=buttons_text['dislike'])
exit_button = KeyboardButton(text=buttons_text['exit'])

search_kb = ReplyKeyboardMarkup(keyboard=[[like_button, dislike_button, exit_button]],
                                resize_keyboard=True)

menu_button = KeyboardButton(text=buttons_text['menu'])

menu_kb = ReplyKeyboardMarkup(keyboard=[[menu_button]],
                              resize_keyboard=True)


resume_search_button = KeyboardButton(text=buttons_text['resume_search'])

after_match_kb = ReplyKeyboardMarkup(keyboard=[[resume_search_button, menu_button]],
                                     resize_keyboard=True)


show_likes_button = KeyboardButton(text=buttons_text['show_likes'])

show_likes_kb = ReplyKeyboardMarkup(keyboard=[[show_likes_button, menu_button]],
                                    resize_keyboard=True)


edit_preferences_button = KeyboardButton(text=buttons_text['edit_preferences'])

preferences_kb = ReplyKeyboardMarkup(keyboard=[[edit_preferences_button, back_button]],
                                     resize_keyboard=True)


bachelor_button_inline = InlineKeyboardButton(text=buttons_text['bachelor'], callback_data='bachelor_degree_picked')
master_button_inline = InlineKeyboardButton(text=buttons_text['master'], callback_data='master_degree_picked')
post_graduate_button_inline = InlineKeyboardButton(text=buttons_text['post_graduate'],
                                                   callback_data='post_graduate_degree_picked')
graduated_button_inline = InlineKeyboardButton(text=buttons_text['graduated'], callback_data='graduated_degree_picked')
male_button_inline = InlineKeyboardButton(text=buttons_text['male'], callback_data='man_gender_picked')
female_button_inline = InlineKeyboardButton(text=buttons_text['female'], callback_data='woman_gender_picked')
add_media_button = KeyboardButton(text=buttons_text['add_media'])
done_media_button = KeyboardButton(text=buttons_text['done_media'])

gender_choice_kb_inline = InlineKeyboardMarkup(inline_keyboard=[[male_button_inline, female_button_inline]])
degree_kb_inline = InlineKeyboardMarkup(inline_keyboard=[[bachelor_button_inline, master_button_inline],
                                                         [post_graduate_button_inline, graduated_button_inline]])
media_kb = ReplyKeyboardMarkup(keyboard=[[add_media_button, done_media_button]],
                               resize_keyboard=True)


man_pref_button_inline = InlineKeyboardButton(text=buttons_text['man_pref'], callback_data='man_gender_preference')
woman_pref_button_inline = InlineKeyboardButton(text=buttons_text['woman_pref'], callback_data='woman_gender_preference')
no_pref_button_inline = InlineKeyboardButton(text=buttons_text['no_pref'], callback_data='no_gender_preference')

gender_pref_kb_inline = InlineKeyboardMarkup(inline_keyboard=[[man_pref_button_inline, woman_pref_button_inline],
                                                              [no_pref_button_inline]])


all_button = KeyboardButton(text=buttons_text['all'])
name_button = KeyboardButton(text=buttons_text['name'])
age_button = KeyboardButton(text=buttons_text['age'])
gender_button = KeyboardButton(text=buttons_text['gender'])
university_button = KeyboardButton(text=buttons_text['university'])
degree_button = KeyboardButton(text=buttons_text['degree'])
study_year_button = KeyboardButton(text=buttons_text['study_year'])
major_button = KeyboardButton(text=buttons_text['major'])
media_button = KeyboardButton(text=buttons_text['media'])
description_button = KeyboardButton(text=buttons_text['description'])
easter_button = KeyboardButton(text=buttons_text['easter'])

edit_profile_kb = ReplyKeyboardMarkup(keyboard=[[all_button, easter_button, back_button],
                                                [name_button, age_button, university_button],
                                                [gender_button, degree_button, study_year_button],
                                                [major_button, media_button, description_button]],
                                      resize_keyboard=True)


leave_as_is_button = KeyboardButton(text=buttons_text['leave_as_is'])

leave_as_is_kb = ReplyKeyboardMarkup(keyboard=[[leave_as_is_button]],
                                     resize_keyboard=True)


male_button = KeyboardButton(text=buttons_text['male'])
female_button = KeyboardButton(text=buttons_text['female'])

gender_kb = ReplyKeyboardMarkup(keyboard=[[male_button, female_button]],
                                resize_keyboard=True)


bachelor_button = KeyboardButton(text=buttons_text['bachelor'])
master_button = KeyboardButton(text=buttons_text['master'])
post_graduate_button = KeyboardButton(text=buttons_text['post_graduate'])
graduated_button = KeyboardButton(text=buttons_text['graduated'])

degree_kb = ReplyKeyboardMarkup(keyboard=[[bachelor_button, master_button],
                                          [post_graduate_button, graduated_button]],
                                resize_keyboard=True)


man_pref_button = KeyboardButton(text=buttons_text['man_pref'])
woman_pref_button = KeyboardButton(text=buttons_text['woman_pref'])
no_pref_button = KeyboardButton(text=buttons_text['no_pref'])

gender_pref_kb = ReplyKeyboardMarkup(keyboard=[[man_pref_button, woman_pref_button],
                                               [no_pref_button]],
                                     resize_keyboard=True)
