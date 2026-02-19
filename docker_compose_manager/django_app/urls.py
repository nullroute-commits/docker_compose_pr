"""URL configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('docker_compose_manager.django_app.api.urls')),
]
