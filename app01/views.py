from django.shortcuts import render
from app01 import models

# Create your views here.
def student_list(request):
    students = models.Student.objects.all()
    return render(request, 'student_list.html', {'students': students})