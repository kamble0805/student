# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),  # This should be the root for the 'students/' URL
    path('add/', views.student_add, name='student-add'),  # URL for adding a new student
    path('update/<int:pk>/', views.student_update, name='student-update'),  # URL for updating student
    path('delete/<int:pk>/', views.student_delete, name='student-delete'),  # URL for deleting student
]
