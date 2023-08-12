from . import views
from django.urls import path
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', views.dashboardview, name='dashboard'),
    path('dashboard/', views.dashboardview, name='dashboard'),
    path('route_planning/', views.route_planning, name='route_planning'),
    path('driver_management/', views.driver_management, name='driver_management'),
    path('vehicle_management/', views.vehicle_management, name='vehicle_management'),
    path('vehicle/insert/', views.vehicleApi, name='addVehicle'),
    path('delivery_tracking/', views.delivery_tracking, name='delivery_tracking'),
    path('vehicle/', views.vehicleApi, name='vehicles'),
    path('driver/', views.driverApi, name='drivers'),
    path('vehicle/remove/<int:vehicle_id>/', views.vehicleApi, name='removeVehicle'),
    path('address/insert/', views.driverApi, name='addAddress'),
    path('driver/insert/', views.driverApi, name='addDriver'),
    path('driver/remove/<int:driver_id>/', views.driverApi, name='removeDriver'),
]
