from django.shortcuts import render

# Create your views here.
def rendTemplate(request):
    myd= {"name":"Arinha"}
    return render(request,'templatesApp/firstTemplate.html',context=myd)