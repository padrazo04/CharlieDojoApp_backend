# Generated by Django 3.1.2 on 2020-11-22 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20201122_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedojostudentbelt',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]