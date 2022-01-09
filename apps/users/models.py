from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female')
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name="added time", default=timezone.now)

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    profile_image = models.ImageField(verbose_name='profile image', upload_to='profile_image/%Y/%m',
                                      default='profile_image/default.jpg')

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register', 'register'),
        ('forget', 'forget password')
    )

    verification_code = models.CharField('verification code', max_length=20)
    email = models.EmailField('email', max_length=50)
    send_type = models.CharField(choices=send_choices, max_length=10)
    send_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'email verification'
        verbose_name_plural = verbose_name
