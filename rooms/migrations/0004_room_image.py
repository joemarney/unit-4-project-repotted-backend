# Generated by Django 5.1.3 on 2024-11-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_plants'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.URLField(default='https://placehold.co/200x200'),
        ),
    ]
