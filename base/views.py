
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
from .models import Address, Assignment, Customer, DeliveryStatus, Driver, Order, Payment, Role, Route, Shipment, Users, Vehicle
import urllib.request
import json
from django.http import JsonResponse
from base.serializers import VehicleSerializer, DriverSerializer, AddressSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


#Login View
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:dashboard')

#Register View
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('base:dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(RegisterPage, self).get(*args, **kwargs)

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


@csrf_exempt
def vehicleApi(request,vehicle_id=None):
    print("Vehicle API Entered")
    if request.method=='GET':
        vehicles = Vehicle.objects.all()
        vehicle_serializer=VehicleSerializer(vehicles,many=True)
        context = {'vehicledata': vehicle_serializer.data}
        return JsonResponse(vehicle_serializer.data,safe=False)
    elif request.method=='POST':
        vehicle_data=JSONParser().parse(request)
        vehicle_serializer=VehicleSerializer(data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        vehicle_data=JSONParser().parse(request)
        vehicle=Vehicle.objects.get(VehicleID=vehicle_data['VehicleID'])
        vehicle_serializer=VehicleSerializer(vehicle,data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        vehicle=Vehicle.objects.get(VehicleID = vehicle_id)
        vehicle.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    print("Vehicle API Exited")


@csrf_exempt
def driverApi(request, driver_id=None):
    print("Driver API Entered")
    if request.method == 'GET':
            drivers = Driver.objects.all()
            driver_serializer = DriverSerializer(drivers, many=True)
            return JsonResponse(driver_serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        print('Driver Data:  ',data)
        driver_data = data['DriverData']
        address_data = data['AddressData']
        address_serializer = AddressSerializer(data=address_data)
        print('validity')
        print(address_serializer.is_valid())
        if address_serializer.is_valid():
            address = address_serializer.save()
            driver_data['AddressID'] = address.AddressID
            driver_serializer = DriverSerializer(data=driver_data)
            if driver_serializer.is_valid():
                driver_serializer.save()
                return JsonResponse({'message': 'Driver added successfully.'})
            else:
                print("Driver Validation Errors:", driver_serializer.errors)
                return JsonResponse({'message': 'Failed to add driver.'}, status=400)
        else:
            print("Address Validation Errors:", address_serializer.errors)
            return JsonResponse({'message': 'Failed to add address.'}, status=400)
    elif request.method == 'PUT':
            driver_data = JSONParser().parse(request)
            driver = Driver.objects.get(DriverID=driver_data['DriverID'])
            driver_serializer = DriverSerializer(driver, data=driver_data)
            if driver_serializer.is_valid():
                driver_serializer.save()
                return JsonResponse("Updated Successfully", safe=False)
            return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
            driver = Driver.objects.get(DriverID=driver_id)
            driver.delete()
            return JsonResponse("Deleted Successfully", safe=False)
    print("Driver API Exited")