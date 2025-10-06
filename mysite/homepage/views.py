# homepage/views.py
from django.http import JsonResponse

# Mock database
students_data = [
    {"id": 1, "name": "Juan", "course": "BSIT"},
    {"id": 2, "name": "Maria", "course": "BSCpE"},
    {"id": 3, "name": "Liza", "course": "BSCS"}
]

# GET all students
def students(request):
    return JsonResponse(students_data, safe=False)

# GET student by ID (parameter)
def student_detail(request, student_id):
    student = next((s for s in students_data if s["id"] == student_id), None)
    if student:
        return JsonResponse(student, safe=False)
    else:
        return JsonResponse({"error": "Student not found"}, status=404)

# GET by query parameter (e.g. ?course=BSIT)
def students_by_course(request):
    course = request.GET.get("course", None)
    if course:
        filtered = [s for s in students_data if s["course"] == course]
        return JsonResponse(filtered, safe=False)
    return JsonResponse(students_data, safe=False)
