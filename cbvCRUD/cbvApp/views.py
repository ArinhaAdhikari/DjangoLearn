from django.shortcuts import render
from django.views.generic import ListView
from cbvApp.models import Student
class StudentListView(ListView):
    model = Student
    # template_name = ".html"


# Create your views here.
