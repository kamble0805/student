# student_management/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Import the RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # Include students app URLs
    path('', RedirectView.as_view(url='/students/', permanent=True)),  # Redirect root URL to /students/
]
