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
        return redirect("Student_home") 

    return render(request, "student/add_student.html")
def delete_student(request, id):
    my_student = Student.objects.get(id=id)
    my_student.delete()
    return redirect("Student_home")

def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone_number")

        student.save()
      
    parameter = {
        "student": student
    }
    return render(request , "student/update_student.html",parameter)