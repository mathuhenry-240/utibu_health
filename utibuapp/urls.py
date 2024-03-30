from utibuapp import views
from django.urls import path


urlpatterns = [

    path('login/',views.login_view,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.register_view,name='register'),
    path('user/', views.userpage,name='user-page'),

    path('products/',views.productsView,name='products'),
    path('customers/<str:pk>/',views.customersView,name='customer'),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('create_order/',views.create_order,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('create_order/',views.create_order,name='create_order'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),
    path('create_customer/',views.create_customer,name='create_customer'),
    path('update_customer/<str:pk>/',views.update_customer,name='update_customer'),
    path('delete_customer/<str:pk>/',views.delete_customer,name='delete_customer'),
]