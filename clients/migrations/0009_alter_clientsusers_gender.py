# Generated by Django 4.1 on 2022-08-31 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_clientsusers_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsusers',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10),
        ),
    ]