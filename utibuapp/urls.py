from utibuapp import views
from django.urls import path


urlpatterns = [
    path('products/',views.productsView,name='products'),
    path('customers/<str:pk>/',views.customersView,name='customer'),
    path('dashboard/',views.dashboardView,name='dashboard')
]