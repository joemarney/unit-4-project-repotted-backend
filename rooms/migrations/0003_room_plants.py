# Generated by Django 5.1.3 on 2024-11-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_remove_plant_owner'),
        ('rooms', '0002_remove_room_dependents'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='plants',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='plants.plant'),
        ),
    ]