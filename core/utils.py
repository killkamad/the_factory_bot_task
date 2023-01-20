import requests

from the_factory_bot_task.settings import TELEGRAM_BOT_TOKEN


def get_chat_id():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    updates = response.json()["result"]
    if len(updates)>0:
        chat_id = updates[-1]["message"]["chat"]["id"]
        return chat_id
    else:
        return None


get_chat_id()