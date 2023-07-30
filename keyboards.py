from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
# ReplyKeyboardRemove


kb = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True
b1 = KeyboardButton('Покажи абезяну')
b2 = KeyboardButton('Покажи кота')
b3 = KeyboardButton('🐈‍⬛')
b4 = KeyboardButton('Рандомная фотка')
kb.add(b1, b2).add(b3, b4)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='VK',
                           url='https://vk.com/warden00')
ib2 = InlineKeyboardButton(text='github',
                           url='https://github.com/germynic31')
ikb.add(ib1).insert(ib2)


kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Рандом')
bp2 = KeyboardButton(text='Главное меню')
kb_photo.add(bp1, bp2)


ikb2 = InlineKeyboardMarkup(row_width=2)
ik1 = InlineKeyboardButton(text='❤️', callback_data='like')
ik2 = InlineKeyboardButton(text='🤮', callback_data='dislike')
ik3 = InlineKeyboardButton(text='Следующая фотка', callback_data='next')
ikb2.add(ik1, ik2).add(ik3)
