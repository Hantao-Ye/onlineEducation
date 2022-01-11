from django.contrib import admin

from apps.courses.models import Course, Lesson
from apps.quizzes.models import Question, QuestionAnswer, Quiz


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'description', 'file', 'question_type']
    search_fields = ['course', 'lesson', 'description', 'question_type']
    list_filter = ['course', 'lesson', 'description', 'file', 'question_type']


class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'answer_type']
    search_fields = ['question', 'answer', 'answer_type']
    list_filter = ['question', 'answer', 'answer_type']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'quiz_type']
    search_fields = ['name', 'quiz_type']
    list_filter = ['name', 'quiz_type']


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)
admin.site.register(Quiz, QuizAdmin)
