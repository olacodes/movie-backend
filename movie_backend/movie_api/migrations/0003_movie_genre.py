# Generated by Django 2.2.7 on 2019-11-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0002_auto_20191127_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]