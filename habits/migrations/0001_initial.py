# Generated by Django 5.0.6 on 2024-05-10 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место выполнения привычки')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='Время выполнения привычки')),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('sign_of_pleasant', models.BooleanField(default=False, verbose_name='Признак наличия приятной привычки или вознаграждения')),
                ('associated_habit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Связанная привычка или вознаграждение')),
                ('frequency', models.IntegerField(default=1, verbose_name='Частота выполнения полезной привычки, в днях')),
                ('time_of_complete', models.IntegerField(default=1, verbose_name='Время за которое совершается привычка, в секундах')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности привычки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]