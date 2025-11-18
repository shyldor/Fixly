from aiogram import Bot, Dispatcher

import aiogram

from myBot.config import telegram_token

bot = Bot(telegram_token)

dp = Dispatcher(bot)
