from django.urls import path
from . import views 

urlpatterns = [
    path("std/",views.student_home),
    path("add/",views.add_student)
]