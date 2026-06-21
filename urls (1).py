from django.urls import path
from .views import register_student, student_list

urlpatterns = [
    path('', register_student, name='register'),
    path('students/', student_list, name='student_list'),
]