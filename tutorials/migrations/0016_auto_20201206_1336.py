# Generated by Django 3.1.2 on 2020-12-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0015_auto_20201206_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedojostudentbelt',
            name='examDate',
            field=models.DateField(),
        ),
    ]
