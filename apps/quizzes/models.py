from django.db import models

from apps.users.models import BaseModel
from apps.courses.models import Course
from apps.courses.models import Lesson

QUESTION_TYPES = (
    ('mcq', 'multiple choice question'),
    ('mcsq', 'multiple choices question'),
    ('tfq', 'true/false question'),
)

ANSWER_TYPES = (
    ('true', 'true'),
    ('false', 'false')
)

QUIZ_TYPES = (
    ('pre-test', 'preview test'),
    ('post-test', 'post test'),
    ('review-test', 'review test')
)


class Question(BaseModel):
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name='lesson', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='question description')
    file = models.FileField(verbose_name='question file', upload_to='quiz/resources/%Y/%m', max_length=200)
    question_type = models.CharField(verbose_name='question type', choices=QUESTION_TYPES, max_length=4)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = verbose_name


class QuestionAnswer(BaseModel):
    question = models.ForeignKey(Question, verbose_name='question', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='question answer')
    answer_type = models.CharField(verbose_name='answer type', choices=ANSWER_TYPES, max_length=4)

    class Meta:
        verbose_name = 'question answer'
        verbose_name_plural = verbose_name


class Quiz(BaseModel):
    name = models.CharField(verbose_name='quiz name', max_length=150)
    questions = models.ManyToManyField(Question)
    quiz_type = models.CharField(verbose_name='quiz type', choices=QUIZ_TYPES, max_length=10)

    class Meta:
        verbose_name = 'quiz'
        verbose_name_plural = verbose_name
