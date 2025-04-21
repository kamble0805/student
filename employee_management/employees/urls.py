# employees/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee-list'),  # Employee list page
    path('add/', views.employee_add, name='employee-add'),  # Add employee page
    path('update/<int:pk>/', views.employee_update, name='employee-update'),  # Update employee page
    path('delete/<int:pk>/', views.employee_delete, name='employee-delete'),  # Delete employee
]
