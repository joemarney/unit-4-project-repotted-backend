# Generated by Django 5.1.3 on 2024-11-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_rename_default_image_plant_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.URLField(default='https://placehold.co/200x200'),
        ),
    ]
