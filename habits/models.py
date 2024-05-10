from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Habits(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец привычки')

    place = models.CharField(max_length=255,
                             verbose_name='Место выполнения привычки',
                             **NULLABLE)

    time = models.DateTimeField(verbose_name='Время выполнения привычки',
                                **NULLABLE)

    action = models.CharField(max_length=255,
                              verbose_name='Действие')

    # В приложении все привычки полезные, добавлять отдельно приятные привычки не вижу смысла, поскольку они всегда
    # завязаны на полезной привычке, отсюда делаем вывод о том, что есть смысл добавить поле о наличии у полезной
    # привычки приятной привычки или вознаграждения и создать валидацию с тем фактом, что если
    # поле sign_of_pleasant = True, то поле associated_habit не может быть пустыми наоборот, поскольку приятной
    # привычки то может и не быть у полезной привычки
    sign_of_pleasant = models.BooleanField(verbose_name='Признак наличия приятной привычки или вознаграждения',
                                           default=False)

    associated_habit = models.CharField(max_length=255,
                                        verbose_name='Связанная привычка или вознаграждение',
                                        **NULLABLE)

    frequency = models.IntegerField(verbose_name='Частота выполнения полезной привычки, в днях',
                                    default=1)

    time_of_complete = models.IntegerField(verbose_name='Время за которое совершается привычка, в секундах',
                                           default=1)

    is_public = models.BooleanField(verbose_name="Признак публичности привычки",
                                    default=False)

    def __str__(self):
        return f'{self.owner} - будет {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
