# Generated by Django 4.0.5 on 2022-07-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0004_remove_chorespost_city_remove_chorespost_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='chorespost',
            name='date_of_post',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
