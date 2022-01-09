from django.contrib import admin

from apps.courses.models import Course, Lecturer, Lesson, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_id']
    search_fields = ['name', 'course_id']
    list_filter = ['name', 'course_id']


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'website']
    search_fields = ['course', 'name', 'website']
    list_filter = ['course', 'name', 'website']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'name']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'name']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name']


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'file']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)
