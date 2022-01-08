# Generated by Django 2.2 on 2022-01-08 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='added time'),
        ),
    ]
