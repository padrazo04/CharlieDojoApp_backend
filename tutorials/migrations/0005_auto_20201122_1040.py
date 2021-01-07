# Generated by Django 3.1.2 on 2020-11-22 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20201122_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDojoStudentBelt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examDate', models.DateField()),
                ('calification', models.CharField(default='no apto', max_length=25)),
                ('attendedClasses', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('belt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.belt')),
                ('studentService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('studentService', 'belt', 'examDate')},
            },
        ),
        migrations.DeleteModel(
            name='StudentBelt',
        ),
        migrations.AlterField(
            model_name='belt',
            name='students',
            field=models.ManyToManyField(through='tutorials.ServiceDojoStudentBelt', to=settings.AUTH_USER_MODEL),
        ),
    ]