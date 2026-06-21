from django.shortcuts import render, redirect
from .models import Student

def register_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            roll_number=request.POST.get("roll_number"),
            contact=request.POST.get("contact"),
            email=request.POST.get("email"),
            address=request.POST.get("address"),
            dob=request.POST.get("dob"),
            course=request.POST.get("course")
        )
        return redirect('/')

    return render(request, "register.html")


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})