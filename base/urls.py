from . import views
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    #path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', views.dashboardview, name='dashboard'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task-create/', TaskCreate.as_view(), name='task_create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('dashboard/', views.dashboardview, name='dashboard'),
    path('route_planning/', views.route_planning, name='route_planning'),
    path('driver_management/', views.driver_management, name='driver_management'),
    path('vehicle_management/', views.vehicle_management, name='vehicle_management'),
    path('delivery_tracking/', views.delivery_tracking, name='delivery_tracking'),
]