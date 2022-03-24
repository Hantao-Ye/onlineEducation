from django.contrib import admin

from apps.courses.models import *


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher_id', 'website']
    search_fields = ['name', 'teacher_id', 'website']
    list_filter = ['name', 'teacher_id', 'website']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_id', 'lecturer']
    search_fields = ['name', 'course_id', 'lecturer']
    list_filter = ['name', 'course_id', 'lecturer']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'lesson_id']
    search_fields = ['course', 'name', 'lesson_id']
    list_filter = ['course', 'name', 'lesson_id']


class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'name', 'file']
    search_fields = ['lesson', 'name', 'file']
    list_filter = ['lesson', 'name', 'file']


class LessonResourceAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'name', 'file']
    search_fields = ['lesson', 'name', 'file']
    list_filter = ['lesson', 'name', 'file']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonVideo, LessonVideoAdmin)
admin.site.register(LessonResource, LessonResourceAdmin)
