from django.shortcuts import render
from django.http import HttpResponse
from app.models import Order

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'order_list.html', context)
