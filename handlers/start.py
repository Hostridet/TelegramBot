from main import dp, types, bot
from handlers.commands import helper
import dictionary
from data.bd_commands import bd_work


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    sti = open('static/sticker.webp', 'rb')
    await bot.send_sticker(message.from_user.id, sti)
    bd = bd_work()
    bd.create()
    users_id = message.from_user.id
    info = bd.find(users_id)
    if not info:
        user_id = [message.from_user.id]
        bd.add(user_id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(dictionary.markup1_message)
    item2 = types.KeyboardButton(dictionary.markup2_message)
    item3 = types.KeyboardButton(dictionary.markup3_message)
    item4 = types.KeyboardButton(dictionary.markup4_message)
    item5 = types.KeyboardButton(dictionary.markup5_message)
    item6 = types.KeyboardButton(dictionary.markup6_message)
    item7 = types.KeyboardButton(dictionary.markup7_message)
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    await bot.send_message(message.from_user.id, dictionary.Welcome_message, reply_markup=markup)
    await helper(message)
