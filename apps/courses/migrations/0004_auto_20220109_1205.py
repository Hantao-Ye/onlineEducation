# Generated by Django 2.2 on 2022-01-09 12:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20220108_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 12, 5, 5, 937078, tzinfo=utc), verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 12, 5, 5, 937078, tzinfo=utc), verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 12, 5, 5, 937078, tzinfo=utc), verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 12, 5, 5, 937078, tzinfo=utc), verbose_name='added time'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 12, 5, 5, 937078, tzinfo=utc), verbose_name='added time'),
        ),
    ]
