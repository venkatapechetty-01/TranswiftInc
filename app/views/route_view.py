from django.shortcuts import render
from django.http import HttpResponse
from app.models import Route

def route_list(request):
    routes = Route.objects.all()
    context = {
        'routes': routes
    }
    return render(request, 'route_list.html', context)
