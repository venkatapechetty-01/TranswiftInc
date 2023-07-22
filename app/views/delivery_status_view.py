from django.shortcuts import render
from django.http import HttpResponse
from app.models import DeliveryStatus

def delivery_status_list(request):
    statuses = DeliveryStatus.objects.all()
    context = {
        'statuses': statuses
    }
    return render(request, 'delivery_status_list.html', context)
