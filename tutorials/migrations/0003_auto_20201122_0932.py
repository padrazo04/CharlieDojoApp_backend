# Generated by Django 3.1.2 on 2020-11-22 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20201121_2219'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicedojostudent',
            unique_together={('serviceDojo', 'student')},
        ),
        migrations.RemoveField(
            model_name='servicedojostudent',
            name='month',
        ),
        migrations.RemoveField(
            model_name='servicedojostudent',
            name='paid',
        ),
    ]
