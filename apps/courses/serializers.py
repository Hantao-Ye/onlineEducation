from rest_framework import serializers

from apps.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['add_time', 'name', 'course_id']
