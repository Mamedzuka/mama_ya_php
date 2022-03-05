from aiogram import Bot
from aiogram.dispatcher import Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_TOKEN  # , ADMIN_IDS
from sys import exit

# объявляем хранение для машины состояний
# storage = MemoryStorage()
# объявляем бота и диспатчер
bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot)
