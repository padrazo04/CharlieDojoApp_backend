# Generated by Django 3.1.2 on 2020-11-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0010_auto_20201122_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateofBirth',
            field=models.DateField(default='1901-01-01'),
        ),
    ]