# Generated by Django 2.2 on 2022-01-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20220109_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='file',
            field=models.FileField(max_length=200, upload_to='course/resources/%Y/%m', verbose_name='course resources file'),
        ),
    ]
