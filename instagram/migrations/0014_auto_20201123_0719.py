# Generated by Django 3.1.3 on 2020-11-23 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0013_auto_20201123_0707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='profile_image',
        ),
    ]
