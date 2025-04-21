# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),  # Set the default route to the product list view
    path('add/', views.product_add, name='product-add'),
    path('<int:pk>/update/', views.product_update, name='product-update'),
    path('<int:pk>/delete/', views.product_delete, name='product-delete'),
]
