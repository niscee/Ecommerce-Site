# Generated by Django 3.0.5 on 2020-10-07 07:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0025_contactmanager'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactManager',
            new_name='CustomerContactManager',
        ),
    ]
