# employee_management/urls.py
from django.contrib import admin
from django.urls import path, include
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee-list'),  # Set the default URL to the employee list view
    path('employees/', include('employees.urls')),  # Include the employees app URLs
]
