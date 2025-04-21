from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.api_urls')),    # API endpoints
    path('', include('employees.urls')),            # HTML views (default)
]
