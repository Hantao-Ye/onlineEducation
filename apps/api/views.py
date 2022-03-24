from rest_framework import viewsets

from apps.api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class EmailVerifyViewSet(viewsets.ModelViewSet):
    queryset = EmailVerifyRecord.objects.all()
    serializer_class = EmailVerifySerializer


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonVideoViewSet(viewsets.ModelViewSet):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer


class LessonResourceViewSet(viewsets.ModelViewSet):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer
