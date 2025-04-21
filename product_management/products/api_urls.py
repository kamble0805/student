from django.urls import path
from . import api_views

urlpatterns = [
    path('products/', api_views.ProductListCreateAPIView.as_view(), name='api-product-list-create'),
    path('products/<int:pk>/', api_views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='api-product-detail'),
]
