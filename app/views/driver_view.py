from django.shortcuts import render
from django.http import HttpResponse
from app.models import Driver

def driver_list(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'driver_list.html', context)
