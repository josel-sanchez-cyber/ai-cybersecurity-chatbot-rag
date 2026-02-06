import telebot
import logging
from config import BOT_TOKEN
from handlers import procesar_mensaje

logging.basicConfig(filename='bot_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot(BOT_TOKEN)
bot.delete_webhook()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    procesar_mensaje(bot, message)

if __name__ == '__main__':
    print("🤖")
    bot.infinity_polling()
