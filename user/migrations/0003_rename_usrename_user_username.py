# Generated by Django 3.2.3 on 2021-05-27 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_usrename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usrename',
            new_name='username',
        ),
    ]
