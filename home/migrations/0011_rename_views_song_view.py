# Generated by Django 3.2.5 on 2021-07-16 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_song_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Views',
            new_name='View',
        ),
    ]
