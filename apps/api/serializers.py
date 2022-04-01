from rest_framework import serializers

from apps.users.models import *
from apps.courses.models import *
from apps.quizzes.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'email']


class EmailVerifySerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailVerifyRecord
        fields = ['verification_code', 'email', 'send_type', 'send_time']


class LecturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'teacher_id', 'website']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'lecturer', 'name', 'course_id']


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'name', 'lesson_id']


class LessonVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonVideo
        fields = ['id', 'lesson', 'name', 'file']


class LessonResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonResource
        fields = ['id', 'lesson', 'name', 'file']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'course', 'lesson', 'description', 'file', 'question_type']


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'questions', 'quiz_type']
