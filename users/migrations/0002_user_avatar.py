# Generated by Django 5.1.3 on 2024-11-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True, default='https://placehold.co/60x60', null=True),
        ),
    ]