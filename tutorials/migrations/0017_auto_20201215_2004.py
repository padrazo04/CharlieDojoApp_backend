# Generated by Django 3.1.2 on 2020-12-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0016_auto_20201206_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='pointsForStudent',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='photo',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]