from django.shortcuts import render
from django.http import HttpResponse
from core.erp.models import Category,Product

# Create your views here.
def miprimeravista (request):
    datos={
        'nombre':'Fatima Naomi',
        'categories':Category.objects.all()
    }
    
    return render(request,"index.html",datos)

def misegundavista (request):
    datos={
        'nombre':'Fatima Naomi',
        'products':Product.objects.all()
    }
    
    return render(request,"second.html",datos)


