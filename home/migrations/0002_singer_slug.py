# Generated by Django 3.2.5 on 2021-07-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='Slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
    ]
