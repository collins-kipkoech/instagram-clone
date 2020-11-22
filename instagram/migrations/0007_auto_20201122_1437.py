# Generated by Django 3.1.3 on 2020-11-22 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20201122_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='profile_pictures'),
        ),
    ]
