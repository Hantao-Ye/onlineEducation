from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'emailVerify', views.EmailVerifyViewSet)
router.register(r'lecturers', views.LecturerViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'lesson', views.LessonViewSet)
router.register(r'lesson_video', views.LessonVideoViewSet)
router.register(r'lesson_resource', views.LessonResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
