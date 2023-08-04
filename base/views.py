from django import forms
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Address, Assignment, Customer, DeliveryStatus, Driver, Order, Payment, Role, Route, Shipment, Task, Users, Vehicle
import urllib.request
import json
from django.http import JsonResponse


# from database_checker import check_database_connection

# def some_view(request):
#     if check_database_connection():
#         print("Connection successful")
#     else:
#         print("Connection unsuccessful")

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:dashboard')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task_list'] = context['task_list'].filter(title__icontains=search_input)

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_detail'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task_list')
    
def dashboardview(request):
    return render(request, 'base/dashboard.html', {'form':forms})

def route_planning(request):
    return render(request, 'base/route_planning.html', {'form':forms})

def driver_management(request):
    return render(request, 'base/driver_management.html', {'form':forms})

def vehicle_management(request):
    return render(request, 'base/vehicle_management.html', {'form':forms})

def delivery_tracking(request):
    return render(request, 'base/delivery_tracking.html', {'form':forms})

def request_page(request):
      if(request.GET.get('mybtn')):

        endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
        # api_file = open("api-key.txt", "r")
        # apikey = api_file.readline()
        # api_file.close()
        apikey = 'AIzaSyAmDjTkOp-6002CzNM1m9ha7KNzGU36p_A'

        origin = request.GET.get('origin', '')
        destination = request.GET.get('destination', '')

        navg_request = f'origin={origin}&destination={destination}&key={apikey}'
        request_url = endpoint + navg_request
        print(request_url)

        try:
            response = urllib.request.urlopen(request_url).read()
            directions = json.loads(response)
            return render(request, 'route_planning.html', JsonResponse(directions))
            #return JsonResponse(directions)
        except Exception as e:
            return JsonResponse({'error': str(e)})


def role_list(request):
    roles = Role.objects.all()
    context = {
        'roles': roles
    }
    return render(request, 'role_list.html', context)

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

def delivery_status_list(request):
    statuses = DeliveryStatus.objects.all()
    context = {
        'statuses': statuses
    }
    return render(request, 'delivery_status_list.html', context)

def address_list(request):
    addresses = Address.objects.all()
    context = {
        'addresses': addresses
    }
    return render(request, 'address_list.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customer_list.html', context)

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

def route_list(request):
    routes = Route.objects.all()
    context = {
        'routes': routes
    }
    return render(request, 'route_list.html', context)

def driver_list(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'driver_list.html', context)

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'assignment_list.html', context)

def shipment_list(request):
    shipments = Shipment.objects.all()
    context = {
        'shipments': shipments
    }
    return render(request, 'shipment_list.html', context)

def insertvehicle(request):
    print("#########")
    vregnumber = request.POST['registrationnumber'];
    vmake = request.POST['make'];
    vmodel = request.POST['model'];
    vcapacity = request.POST['capacity'];
    us = Vehicle(RegistrationNumber = vregnumber, Make = vmake, Model = vmodel, Capacity = vcapacity);
    us.save();
    print("#########")
    return render(request, 'dashboard.html' , {})
    



