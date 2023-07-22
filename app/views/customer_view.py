from django.shortcuts import render
from django.http import HttpResponse
from app.models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customer_list.html', context)
