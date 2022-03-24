from django.db import models

from apps.users.models import BaseModel


class Lecturer(BaseModel):
    name = models.CharField(verbose_name='lecturer name', max_length=20)
    teacher_id = models.CharField(verbose_name='teacher id number', max_length=10, unique=True)
    website = models.URLField(verbose_name='lecturer link',)

    class Meta:
        verbose_name = 'course lecturer'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_id + self.name


class Course(BaseModel):
    name = models.CharField(verbose_name='course name', max_length=50)
    course_id = models.CharField(verbose_name='course id number', max_length=10, unique=True)

    lecturer = models.ForeignKey(Lecturer, verbose_name='lecturer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'course information'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_id + " " + self.name


class Lesson(BaseModel):
    name = models.CharField(verbose_name='lesson name', max_length=50)
    lesson_id = models.CharField(verbose_name='chapter number', max_length=10)

    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE, related_name="Course")

    class Meta:
        verbose_name = 'course lesson'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.course_id + " " + self.lesson_id + " " + self.name


class LessonVideo(BaseModel):
    name = models.CharField(verbose_name='video name', max_length=100)
    file = models.FileField(verbose_name='video file', upload_to='courses/video/', max_length=200)

    lesson = models.ForeignKey(Lesson, verbose_name='lesson', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'course video'
        verbose_name_plural = verbose_name


class LessonResource(BaseModel):
    name = models.CharField(verbose_name='course resources', max_length=50)
    file = models.FileField(verbose_name='course resources file', upload_to='courses/resources/', max_length=200)

    lesson = models.ForeignKey(Lesson, verbose_name='lesson', on_delete=models.CASCADE)

    # @property
    # def course_id(self):
    #     return self.lesson.course.course_id

    class Meta:
        verbose_name = 'course resources'
        verbose_name_plural = verbose_name
