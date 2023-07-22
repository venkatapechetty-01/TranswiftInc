from django.shortcuts import render
from django.http import HttpResponse
from app.models import Assignment

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments
    }
    return render(request, 'assignment_list.html', context)
