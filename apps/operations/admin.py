from django.contrib import admin

from apps.operations.models import UserCourse


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course']


admin.site.register(UserCourse, UserCourseAdmin)
