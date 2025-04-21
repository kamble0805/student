from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.api_urls')),  # REST API endpoints
    path('', include('products.urls')),          # HTML web interface
]
