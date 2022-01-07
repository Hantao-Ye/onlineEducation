from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female')
)


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name='nick name', max_length=50, default='')
    birthday = models.DateField(verbose_name='birthday', null=True, blank=True)
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(verbose_name='address', max_length=100, default='')
    mobile = models.CharField(verbose_name='mobile', max_length=11, unique=True)
    profile_image = models.ImageField(verbose_name='profile image', upload_to='profile_image/%Y/%m',
                                      default='profile_image/default.jpg')

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name

        return self.username
