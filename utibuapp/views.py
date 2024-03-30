from django.shortcuts import render,redirect
from django.http import HttpResponse
from utibuapp.models import Customer,Product,Order
from .forms import OrderForm,CustomerForm,CreateUserForm
from django.contrib import messages


# Create your views here.

def login_view(request):
    context = {}
    return render(request,'accounts/login.html',context)

def register_view(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account was created for' + user)
            return redirect('login')
        else:
            messages.warning(request,'account was not created')
            return redirect('register')
    context = {'form':form}
    return render(request,'accounts/register.html',context)

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


def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'accounts/create_customer.html',context)

def update_customer(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'accounts/create_customer.html',context)

def delete_customer(request,pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('dashboard')
    context = {'customer':customer}
    return render(request,'accounts/delete_customer.html',context)


def productsView(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'accounts/products.html',context)


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        # print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')

    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    
    context={'item':order}
    return render(request,'accounts/delete_form.html',context)

