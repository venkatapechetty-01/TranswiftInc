from django.shortcuts import render
from django.http import HttpResponse
from app.models import Role

def get_roles(request):
    # Query the database to get all roles from the Role model
    roles = Role.objects.all()

    for role in roles:
        print(f"RoleID: {role.RoleID}, RoleName: {role.RoleName}")

def role_list(request):
    roles = Role.objects.all()
    context = {
        'roles': roles
    }
    return render(request, 'role_list.html', context)
