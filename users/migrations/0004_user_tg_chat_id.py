# Generated by Django 5.0.6 on 2024-05-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_tg_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='tg_chat_id'),
        ),
    ]
