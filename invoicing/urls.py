from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.staff_login, name='login'),
    path('invoices/', views.view_invoice, name='view_invoice'),
    
    
    path('chef/dashboard/', views.chef_dashboard, name='chef_dashboard'),
    path('cashier/dashboard/', views.cashier_dashboard, name='cashier_dashboard'),

    path('orders/today/', views.view_orders, name='view_orders'),
    path('menu/update/', views.update_availability, name='update_availability'),

]
