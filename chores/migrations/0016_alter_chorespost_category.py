# Generated by Django 4.0.5 on 2022-07-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0015_remove_chorespost_id_chorespost_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chorespost',
            name='category',
            field=models.CharField(choices=[('1', 'majstor'), ('2', 'korisnik')], max_length=100),
        ),
    ]
