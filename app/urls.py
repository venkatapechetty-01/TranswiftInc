from django.urls import path
from app import views

urlpatterns = [
    # Define app's URL patterns here
    path('users/', views.user_list, name='user_list'),
    path('roles/', views.role_list, name='role_list'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('drivers/', views.driver_list, name='driver_list'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('delivery_statuses/', views.delivery_status_list, name='delivery_status_list'),
    path('addresses/', views.address_list, name='address_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('routes/', views.route_list, name='route_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
]
