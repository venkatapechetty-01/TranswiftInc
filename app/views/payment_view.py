from django.shortcuts import render
from django.http import HttpResponse
from app.models import Payment

def payment_list(request):
    payments = Payment.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'payment_list.html', context)
