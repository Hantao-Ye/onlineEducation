from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile
from apps.users.models import EmailVerifyRecord


class UserProfileAdmin(admin.ModelAdmin):
    pass


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['verification_code', 'email', 'send_type', 'send_time']
    search_fields = ['verification_code', 'email', 'send_type']
    list_filter = ['verification_code', 'email', 'send_type', 'send_time']


admin.site.register(UserProfile, UserAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
