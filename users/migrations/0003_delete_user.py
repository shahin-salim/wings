# Generated by Django 4.0.4 on 2022-05-16 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_nickname_user_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
