from django.shortcuts import render
from django.http import HttpResponse
from app.models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehicle_list.html', context)
