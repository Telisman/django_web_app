# Generated by Django 4.0.5 on 2022-07-19 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chores', '0019_alter_chorespost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='chorespost',
            name='user_of_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
