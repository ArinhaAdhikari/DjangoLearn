from django.shortcuts import render
from clinicalsApp.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
from django.shortcuts import redirect,render

class PatientListView(ListView):
    model=Patient
    
class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')

def addData(request,**kwargs):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])#get that perticular patient
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form,'patient':patient})

def analyze(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])#get all data of that patient ,this is a query set
    responseData=[]
    for eachEntry in data:
        if eachEntry.componentName=='hw':  #to calculate the bmi
            heightandweight=eachEntry.componentValue.split('/') #split the string having hight and weight in h/w format
            if len(heightandweight)>1:
                feettomtr=float(heightandweight[0])*0.4536
                BMI=(float(heightandweight[1]))/(feettomtr*feettomtr)
                bmientry=ClinicalData()
                bmientry.componentName='BMI'
                bmientry.componentValue=BMI
                responseData.append(bmientry)
        responseData.append(eachEntry)
        
    return render(request,'clinicalsApp/generateReport.html',{'data':responseData})
    
# Create your views here.
