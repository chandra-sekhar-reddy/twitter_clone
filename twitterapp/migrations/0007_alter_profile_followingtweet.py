# Generated by Django 4.2.1 on 2023-05-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0006_profile_followingtweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followingtweet',
            field=models.JSONField(default=list, verbose_name=models.TextField()),
        ),
    ]
