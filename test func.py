# from random import randrange
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


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(f"Вот id твоего стикера: {message.sticker.file_id}")

# import string
# import random
@dp.message_handler()
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.reply('yes')
    else:
        await message.reply('no')