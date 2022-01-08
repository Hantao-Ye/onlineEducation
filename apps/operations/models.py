from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

UserProfile = get_user_model()


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'user courses'
        verbose_name_plural = verbose_name
