# Generated by Django 3.2.5 on 2024-09-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/static/images/profiles/default.png', upload_to='static/images/profiles/'),
        ),
    ]