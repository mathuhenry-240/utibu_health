from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboardView(request):
    return render(request,'accounts/dashboard.html')

def customersView(request):
    return render(request,'accounts/customers.html')


def homeView(request):
    return render(request,'accounts/home.html')


def productsView(request):
    return render(request,'accounts/products.html')
