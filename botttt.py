# -*- coding: utf-8 -*-

import telebot
import random


from aiogram.utils import executor

from telebot import *
from telegram.ext import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG, filename='app.log', filemode='a')

logger = logging.getLogger(__name__)
TOKEN = 'token'
bot = telebot.TeleBot(TOKEN, threaded=False)
dp = Dispatcher(bot, update_queue=False)
MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates'.format(token=TOKEN)
if __name__ == '__main_':
    executor.start_polling(dp, skip_updates=True)


@bot.message_handler(content_types=['new_chat_members'])
def lalala(message):
    if message.chat.type == 'supergroup':
        word = ["Привет, бот", "Привіт, бот", "Hello, bot"]
        bot.send_message(message.chat.id, random.sample(word, 1))



while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        logger.error(e)
        time.sleep(5)