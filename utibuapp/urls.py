from utibuapp import views
from django.urls import path


urlpatterns = [
    path('',views.homeView,name='home'),
    path('products/',views.productsView,name='products'),
    path('customers/',views.customersView,name='customers'),
    path('dashboard/',views.dashboardView,name='dashboard')
]