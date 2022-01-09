# Generated by Django 2.2 on 2022-01-09 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220108_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_code', models.CharField(max_length=20, verbose_name='verification code')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('send_type', models.CharField(choices=[('register', 'register'), ('forget', 'forget password')], max_length=10)),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'email verification',
                'verbose_name_plural': 'email verification',
            },
        ),
    ]
