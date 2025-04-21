# employees/api_urls.py
from django.urls import path
from . import api_views

urlpatterns = [
    path('employees/', api_views.EmployeeListCreateAPIView.as_view(), name='api-employee-list-create'),
    path('employees/<int:pk>/', api_views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='api-employee-detail'),
]
