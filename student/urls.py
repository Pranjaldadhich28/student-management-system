from django.urls import path
from . import views 

urlpatterns = [
    path("std/",views.student_home,name = "Student_home"),
    path("add/",views.add_student,name = "add_student"),
    path("delete_student/<int:id>",views.delete_student,name = "delete_student"),
    path("update_student/<int:id>",views.update_student,name="update_student"),
]