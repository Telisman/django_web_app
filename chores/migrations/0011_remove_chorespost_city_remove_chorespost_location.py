# Generated by Django 4.0.5 on 2022-07-19 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0010_chorespost_city_chorespost_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chorespost',
            name='city',
        ),
        migrations.RemoveField(
            model_name='chorespost',
            name='location',
        ),
    ]
