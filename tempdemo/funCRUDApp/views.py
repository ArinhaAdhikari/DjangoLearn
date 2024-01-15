from django.shortcuts import render,redirect
from funCRUDApp.models import Student
from funCRUDApp.forms import StudentForm

def getStudents(request):
    students=Student.objects.all()
    return render(request,'templatesApp/funCRUD.html',{'students':students})

def createStudent(request):
    form=StudentForm()
    if request.method=='POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'templatesApp/create.html',{'form':form})

def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')
def updateStudent(request, id):
    student= Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST, instance=student)
        # instance send to ensure the entire previous row daya is not lost on update it holds the data of unaltered row
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'templatesApp/update.html',{'student':student})

# Create your views here.
