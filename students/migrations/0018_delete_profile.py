# Generated by Django 3.1 on 2020-08-19 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_remove_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
