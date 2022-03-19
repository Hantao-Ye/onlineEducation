from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.courses import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]