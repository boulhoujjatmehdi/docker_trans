# Generated by Django 3.2.5 on 2024-09-21 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
