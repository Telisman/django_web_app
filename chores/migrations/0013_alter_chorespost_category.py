# Generated by Django 4.0.5 on 2022-07-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0012_chorespost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chorespost',
            name='category',
            field=models.CharField(choices=[(1, 'Vodoinstaleter'), (2, 'Eelektricar')], max_length=100),
        ),
    ]
