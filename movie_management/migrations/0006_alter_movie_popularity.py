# Generated by Django 5.0 on 2023-12-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_management', '0005_movie_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(default=None),
        ),
    ]