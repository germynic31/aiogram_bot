from aiogram import Bot, Dispatcher, executor, types
from random import randrange
import random
from keyboards import kb, ikb, kb_photo, ikb2
from config import TOKEN_API
from aiogram.dispatcher.filters import Text
# import string
# import random


HELP_COMMAND = '''
<b>/start</b> - <em>начать работу с ботом и открыть клавиатуру</em>
<b>/links</b> - <em>ссылки на соцсети</em>

<b>Все остальное снизу на клавиатуре</b>
'''


arr_photo = ["https://images.albertsons-media.com/is/image/ABS/184080250?$ng-ecom-pdp-desktop$&defaultImage=Not_Available",
             "https://target.scene7.com/is/image/Target/GUEST_3e3023d6-31c9-4a50-8d1e-a5a5719448ae",
             "https://target.scene7.com/is/image/Target/GUEST_c9cc2d3f-d31a-4e81-a99c-f7521195cd86?wid=488&hei=488&fmt=pjpeg"]

photos = dict(zip(arr_photo, ['лимон', 'лайм', 'грейпфрут']))


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("бот был запущен")

random_photo = random.choice(list(photos.keys()))


async def send_random(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb2)


# func
@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()


@dp.message_handler(Text(equals="Рандомная фотка"))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Что бы отправить рандомную фотку нажми на "Рандом"',
                         reply_markup=kb_photo)
    await message.delete()


@dp.message_handler(Text(equals="Рандом"))
async def send_random_photo2(message: types.Message):
    await send_random(message)


@dp.message_handler(Text(equals="Главное меню"))
async def open_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_sticker(message.chat.id,
                           sticker="CAACAgIAAxkBAAEJ0GtkwCJ3ULrn40xGxy8vOz8Yk_nLogACBQADwDZPE_lqX5qCa011LwQ")
    await message.answer(text='<em>Привет!</em>', parse_mode="HTML", reply_markup=kb)
    await message.delete()


@dp.message_handler(commands='links')
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Вот ссылки на соцсети',
                           reply_markup=ikb)


@dp.message_handler(commands='georandom')
async def send_random_geo(message: types.Message):
    await message.answer("Вот рандомная геолокация")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(-90, 90),
                            longitude=randrange(-180, 180))
    await message.delete()


@dp.message_handler(commands='kr')
async def krasnodar_location(message: types.Message):
    await message.answer("Вот где находится Краснодар на карте")
    await bot.send_location(chat_id=message.chat.id, latitude=45.0448, longitude=38.976)
    await message.delete()


@dp.message_handler(text='Покажи кота')
async def send_cat(message: types.Message):
    await message.answer("Смотри какой кот")
    num = randrange(1, 4)
    if num == 1:
        await bot.send_photo(chat_id=message.chat.id, photo="https://avatars.dzeninfra.ru/get-zen_doc/5233619/pub_6236"
                                                            "38833c14f46c08058ef4_623638c0b4e657033dc6eb87/scale_1200")
    if num == 2:
        await bot.send_photo(chat_id=message.chat.id, photo="https://s13.stc.yc.kpcdn.net/sha"
                                                            "re/i/instagram/B44solahwlo/wr-1280.webp")
    if num == 3:
        await bot.send_photo(chat_id=message.chat.id, photo="https://wl-adme.cf.tsp.li/resize/728"
                                                            "x/jpg/a0a/9c6/6c8266551398ae6d3bf7200468.jpg")


@dp.message_handler(text='Покажи абезяну')
async def send_monkey(message: types.Message):
    await message.answer("Смотри какая абезяна")
    await bot.send_sticker(message.chat.id,
                           sticker="CAACAgIAAxkBAAEJ0W9kwQUDfsFmcCO_b2EAAUdqaJqoY7kAAssVAAJbUjhKdK-4j7qsbJgvBA")


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(f"Вот id твоего стикера: {message.sticker.file_id}")


@dp.message_handler(text='🐈‍⬛')
async def send_black_cat(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAIB52TCwG1LjvcBOHkNenNyA1ekAg7TAALXFQACOeLQS57DiQEzhk9kLwQ')


@dp.callback_query_handler()
async def photo_random_callback(callback: types.CallbackQuery):
    global random_photo
    if callback.data == 'dislike':
        await callback.answer(text="Тебе не понравилось(")
        # await callback.message.answer(text="Тебе не понравилось(")
    elif callback.data == 'like':
        await callback.answer(text="Тебе понравилось")
        # await callback.message.answer(text="Тебе понравилось")
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo, type='photo', caption=photos[random_photo]), reply_markup=ikb2)
        await callback.answer()


# @dp.message_handler()
# async def send_random_letter(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))


# @dp.message_handler()
# async def check_zero(message: types.Message):
#     if '0' in message.text:
#         await message.reply('yes')
#     else:
#         await message.reply('no')

# start


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
