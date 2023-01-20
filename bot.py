import telebot
from the_factory_bot_task.settings import TELEGRAM_BOT_TOKEN
import requests

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(func=lambda m: m.text.startswith("token"))
def handle_token(message):
    token = message.text[5:]
    r = requests.post('http://161.35.199.25/api/check-token/', json={
        "chat_id": message.chat.id,
        "token": token
    })
    print(r)
    bot.reply_to(message, r.json()['message'])

bot.polling()