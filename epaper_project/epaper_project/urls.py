# epaper_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('epaper.urls')),  # Include the urls from the epaper app
]
