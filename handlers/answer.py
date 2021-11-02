from main import dp, bot, types
from data.bd_commands import bd_work
from aiogram.dispatcher import filters
import src
import dictionary
import time
import config


def isBanned(user_id):
    bd = bd_work()
    if str(user_id) in bd.banlist():
        return True
    return False


@dp.message_handler(filters.Text(contains=dictionary.markup7_message))
async def send_my_photo(message: types.Message):
    if not isBanned(message.from_user.id):
        photo = open('static/myphoto.jpg', 'rb')
        await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(filters.Text(contains=dictionary.markup6_message))
async def send_currency(message: types.Message):
    if not (isBanned(message.from_user.id)):
        curs = src.Currency()
        await bot.send_message(message.from_user.id, curs.get_currency())


@dp.message_handler(filters.Text(contains=dictionary.markup5_message))
async def send_info(message: types.Message):
    if not (isBanned(message.from_user.id)):
        await bot.send_message(message.from_user.id, dictionary.help_message)


@dp.message_handler(filters.Text(contains=dictionary.markup4_message))
async def send_joke(message: types.Message):
    if not (isBanned(message.from_user.id)):
        new_joke = src.joker()
        await bot.send_message(message.from_user.id, new_joke.GetJoke())


@dp.message_handler(filters.Text(contains=dictionary.markup3_message))
async def send_weather(message: types.Message):
    if not (isBanned(message.from_user.id)):
        weathers = src.open_weather()
        await bot.send_message(message.from_user.id, weathers.get_weather(config.your_city))


@dp.message_handler(filters.Text(contains=dictionary.markup2_message))
async def send_schedule(message: types.Message):
    if not (isBanned(message.from_user.id)):
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Сегодня", callback_data='today')
        item2 = types.InlineKeyboardButton("Завтра", callback_data='tomorrow')
        markup.add(item1, item2)
        await bot.send_message(message.from_user.id, "На какой день расписание?", reply_markup=markup)


@dp.message_handler(filters.Text(contains=dictionary.markup1_message))
async def send_news(message: types.Message):
    if not (isBanned(message.from_user.id)):
        news = src.News()
        data = news.GetNews()
        i = 0
        while i < news.GetCount():
            await bot.send_message(message.from_user.id, data[i] + "\n" + data[i + 1])
            i += 2
            time.sleep(5)
