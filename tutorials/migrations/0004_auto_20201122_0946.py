# Generated by Django 3.1.2 on 2020-11-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20201122_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateofBirth',
            field=models.DateField(),
        ),
    ]
