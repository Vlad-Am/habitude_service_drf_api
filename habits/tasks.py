from datetime import date, datetime, timedelta
import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habits


@shared_task
def send_tg_message():
    """Функция определяет пользователя которому надо напомнить о выполнении привычки и отправляет ему соответсвующее
     сообщение с частотой выбранной в frequency"""
    url = settings.TELEGRAM_URL
    api_of_bot = settings.API_OF_BOT

    time_now = datetime.now().time().replace(second=0, microsecond=0)
    date_now = date.today()
    habits_to_send = Habits.objects.filter(owner__is_active=True)

    for habit in habits_to_send:
        chat_id = habit.owner.tg_chat_id
        text = f"Вам нужно {habit.action} в {habit.time} в {habit.place}"

        if habit.date_send_message == date_now and habit.time <= time_now:
            requests.get(url=f"{url}{api_of_bot}/sendMessage", data={"chat_id": chat_id, "text": text})
            if date_now - habit.data < timedelta(days=habit.frequency):
                habit.date_send_message = date_now + timedelta(days=1)
                habit.save()
