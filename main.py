from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config


bot = Bot(token=config.token)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
