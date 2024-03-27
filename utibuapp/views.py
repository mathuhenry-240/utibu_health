from django.shortcuts import render
from django.http import HttpResponse
from utibuapp.models import Customer,Product,Order

# Create your views here.

def dashboardView(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = Customer.objects.all().count()
    total_orders = Order.objects.all().count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'customers':customers,'orders':orders,'total_customers':total_customers,
               'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request,'accounts/dashboard.html',context)

def customersView(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer,'orders':orders,'order_count':order_count}

    return render(request,'accounts/customers.html',context)




def productsView(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'accounts/products.html',context)
