from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.api_urls')),     # API endpoints
    path('', include('students.urls')),             # HTML views
]
