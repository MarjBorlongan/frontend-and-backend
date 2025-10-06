# mysite/urls.py
from django.contrib import admin
from django.urls import path
from homepage.views import students, student_detail, students_by_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', students),                     # GET all
    path('students/<int:student_id>/', student_detail),  # GET by ID
    path('students/filter/', students_by_course),    # GET by query
]
