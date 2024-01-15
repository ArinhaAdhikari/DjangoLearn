from django.shortcuts import render
from modelFormApp.forms import ProjectForm
from modelFormApp.models import Project
# Create your views here.m modelForms
def index(request):
    return render(request,'templatesApp/index.html')
def listProjects(request):
    projectsList=Project.objects.all()
    return render(request,'templatesApp/listProjects.html',{'projects': projectsList})
def addProject(request):
    form =ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'templatesApp/addProject.html',{'form':form})