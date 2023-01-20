import requests
from the_factory_bot_task.celery import app
from the_factory_bot_task.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_URL
from core.models import Messages


@app.task
def send_telegram_message(message_id):
    message = Messages.objects.get(id=message_id)
    msg_text = f'<b>{message.user.username}</b>, я получил от тебя сообщение:\n' \
               f'<i>{message.message_body}</i>'
    requests.get(TELEGRAM_URL.format(token=TELEGRAM_BOT_TOKEN, user_id=message.user.telegram_id, msg_text=msg_text))