# Generated by Django 2.2.7 on 2019-11-27 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comedy',
            new_name='Movie',
        ),
    ]