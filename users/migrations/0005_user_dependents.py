# Generated by Django 5.1.3 on 2024-11-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dependents',
            field=models.CharField(blank=True, default='no', null=True),
        ),
    ]
