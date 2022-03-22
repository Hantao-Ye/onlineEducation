from rest_framework import serializers

from apps.users.models import *
from apps.courses.models import *


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name', 'course_id']


class LecturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecturer
        fields = ['course', 'name', 'website']


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['course', 'name']


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['course', 'name']


class CourseResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseResource
        fields = ['course', 'name', 'file']
