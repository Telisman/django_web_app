# Generated by Django 4.1 on 2022-08-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0003_auto_20190617_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
