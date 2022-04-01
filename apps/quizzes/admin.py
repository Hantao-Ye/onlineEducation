from django.contrib import admin

from apps.courses.models import Course, Lesson
from apps.quizzes.models import Question, Quiz


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'description', 'file', 'question_type']
    search_fields = ['course', 'lesson', 'description', 'question_type']
    list_filter = ['course', 'lesson', 'description', 'file', 'question_type']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'quiz_type']
    search_fields = ['name', 'quiz_type']
    list_filter = ['name', 'quiz_type']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
