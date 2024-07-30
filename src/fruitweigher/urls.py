# fruitweigher/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('useraccounts.urls', namespace='useraccounts')),
]
