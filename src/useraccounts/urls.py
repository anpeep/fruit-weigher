# useraccounts/urls.py
from django.urls import path
from useraccounts.views import login_signup_view, home_view, admin_page_view, user_dashboard_view, admin_dashboard_view
from products.views import product_delete_view  # Ensure this import matches the location of product_delete_view

app_name = 'useraccounts'

urlpatterns = [
    path('', login_signup_view, name='login-signup'),
    path('home/', home_view, name='home'),
    path('admin/', admin_page_view, name='admin-page'),
    path('admin/dashboard/', admin_dashboard_view, name='admin-dashboard'),
    path('user/dashboard/', user_dashboard_view, name='user-dashboard'),
    path('products/<int:pk>/delete/', product_delete_view, name='product-delete'),
]
