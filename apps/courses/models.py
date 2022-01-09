from django.db import models

from apps.users.models import BaseModel


class Course(BaseModel):
    name = models.CharField(verbose_name='course name', max_length=50)
    course_id = models.CharField(verbose_name='course id number', max_length=10, unique=True)

    class Meta:
        verbose_name = 'course information'
        verbose_name_plural = verbose_name


class Lecturer(BaseModel):
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='lecturer name', max_length=20)
    website = models.URLField(verbose_name='lecturer link',)

    class Meta:
        verbose_name = 'course lecturer'
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='lesson name', max_length=50)

    class Meta:
        verbose_name = 'course lesson'
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name='lesson', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='video name', max_length=100)
    # file = models.FileField(verbose_name='video file', upload_to='course/videos/%Y/%m', max_length=200)

    class Meta:
        verbose_name = 'course video'
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='course resources', max_length=50)
    file = models.FileField(verbose_name='course resources file', upload_to='course/resources/%Y/%m', max_length=200)

    class Meta:
        verbose_name = 'course resources'
        verbose_name_plural = verbose_name
