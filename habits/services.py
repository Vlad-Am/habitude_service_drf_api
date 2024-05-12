import os

import requests
from django.conf import settings


def send_telegram_message(tg_chat_id, message):
    params = {
        'chat_id': tg_chat_id,
        'text': message
    }
    url = settings.TELEGRAM_URL
    api_of_bot = settings.API_OF_BOT
    requests.get(f"{url}{api_of_bot}/sendMessage", params=params)

