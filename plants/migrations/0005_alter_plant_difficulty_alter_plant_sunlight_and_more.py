# Generated by Django 5.1.3 on 2024-11-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_alter_plant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='difficulty',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sunlight',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='plant',
            name='toxicity',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='plant',
            name='watering',
            field=models.CharField(max_length=8),
        ),
    ]
