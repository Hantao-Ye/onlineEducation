from django.test import TestCase

from apps.courses.models import Course


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(name="Test Course C", course_id="TEST0003")

    def test_name_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.name}'
        self.assertEquals(expected_object_name, 'Test Course C')

    def test_course_id_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.course_id}'
        self.assertEquals(expected_object_name, 'TEST0003')
