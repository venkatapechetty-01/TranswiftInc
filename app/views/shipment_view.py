from django.shortcuts import render
from django.http import HttpResponse
from app.models import Shipment

def shipment_list(request):
    shipments = Shipment.objects.all()
    context = {
        'shipments': shipments
    }
    return render(request, 'shipment_list.html', context)
