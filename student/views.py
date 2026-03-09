from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def student_home(request):
    student_data = Student.objects.all()

    data = {
        "student_data":student_data
    }
    return render(request,"student/student.html",data)
def add_student(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone_number")
        email = request.POST.get("email")

        Student.objects.create(
           name=name,
            email=email,
            phone_number=phone
        )
        return redirect("/student/std/")

    return render(request, "student/add_student.html")
