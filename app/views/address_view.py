from django.shortcuts import render
from django.http import HttpResponse
from app.models import Address

def address_list(request):
    addresses = Address.objects.all()
    context = {
        'addresses': addresses
    }
    return render(request, 'address_list.html', context)
