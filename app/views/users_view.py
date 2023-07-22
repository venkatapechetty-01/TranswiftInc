from django.shortcuts import render
from django.http import HttpResponse
from app.models import Users

def user_list(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_list.html', context)
