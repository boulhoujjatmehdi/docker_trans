# Generated by Django 3.2.5 on 2024-09-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', upload_to='staticfiles/images/profiles/'),
        ),
    ]
