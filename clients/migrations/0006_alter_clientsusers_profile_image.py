# Generated by Django 4.1 on 2022-08-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_clientsusers_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsusers',
            name='profile_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
