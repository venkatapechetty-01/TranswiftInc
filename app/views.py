from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from app.models.address import Address
from app.models.assignment import Assignment
from app.models.customer import Customer
from app.models.delivery_status import DeliveryStatus
from app.models.driver import Driver
from app.models.order import Order
from app.models.payment import Payment
from app.models.role import Role
from app.models.route import Route
from app.models.shipment import Shipment
from app.models.users import Users
from app.models.vehicle import Vehicle

def index(request):
    return render(request, 'TranswiftInc/index.html') #returns the index.html template

def user_list(request):
    # Your view logic here
    return HttpResponse('Hello, users!')

class CustomLoginView(LoginView):
    template_name = '/dashboard.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(RegisterPage, self).get(*args, **kwargs)


def address_list(request):
    addresses = Address.objects.all()
    context = {
        'addresses': addresses
    }
    return render(request, 'address_list.html', context)

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'assignment_list.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customer_list.html', context)

def delivery_status_list(request):
    statuses = DeliveryStatus.objects.all()
    context = {
        'statuses': statuses
    }
    return render(request, 'delivery_status_list.html', context)

def driver_list(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'driver_list.html', context)

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'order_list.html', context)

def payment_list(request):
    payments = Payment.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'payment_list.html', context)

def role_list(request):
    roles = Role.objects.all()
    context = {
        'roles': roles
    }
    return render(request, 'role_list.html', context)

def route_list(request):
    routes = Route.objects.all()
    context = {
        'routes': routes
    }
    return render(request, 'route_list.html', context)

def shipment_list(request):
    shipments = Shipment.objects.all()
    context = {
        'shipments': shipments
    }
    return render(request, 'shipment_list.html', context)

def user_list(request):
    # Your view logic here
    return HttpResponse('Hello, users!')

def users_list(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_list.html', context)

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehicle_list.html', context)

