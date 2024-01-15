from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={'product1':'Mac','product2':'Macbook','product3':'watch'}
    return render(request,'templatesApp/product.html',product_dict)

def toys(request):
    product_dict={'product1':'remte car','product2':'teady','product3':'drone'}
    return render(request,'templatesApp/product.html',product_dict)

def shoes(request):
    product_dict={'product1':'reebok','product2':'woodland','product3':'khadim'}
    return render(request,'templatesApp/product.html',product_dict)
def index(request):
    return render(request,'templatesApp/index.html')
