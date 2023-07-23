from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  
    # Include the app-level URLs here
    # Add more project-level URLs as needed
]