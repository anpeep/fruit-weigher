# products/urls.py
from django.urls import path
from .views import product_delete_view

app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', product_delete_view, name='product-delete'),
]
