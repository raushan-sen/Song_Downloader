# Generated by Django 3.2.5 on 2021-07-12 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_singer_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='Slug',
            field=models.SlugField(blank=True, default='hudshyfu', max_length=40, null=True, unique=True),
        ),
    ]
