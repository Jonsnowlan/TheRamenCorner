# Generated by Django 4.0.4 on 2022-05-31 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ramenCorner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ramencorner',
            old_name='video_url',
            new_name='videoUrl',
        ),
    ]
