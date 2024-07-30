from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product, ProductEntry
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product, ProductEntry

class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

def login_signup_view(request):
    if not User.objects.filter(email='test@gmail.com').exists():
        admin_user = User.objects.create_user(username='admin', email='test@gmail.com')
        admin_user.set_password('Parool1!')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

    login_form = EmailAuthenticationForm()
    signup_form = UserCreationForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = EmailAuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                if user.email == 'test@gmail.com':
                    return redirect('useraccounts:admin-page')
                else:
                    return redirect('useraccounts:user-dashboard')
            else:
                for field, errors in login_form.errors.items():
                    for error in errors:
                        messages.error(request, error, extra_tags='login')
        elif 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, 'Account created successfully. Please login.', extra_tags='signup success')
                return redirect('useraccounts:login-signup')
            else:
                for field, errors in signup_form.errors.items():
                    for error in errors:
                        messages.error(request, error, extra_tags='signup')

    return render(request, 'account/login_signup.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })


@login_required
def home_view(request):
    if request.user.email == 'test@gmail.com':  # Admin email check
        return redirect('useraccounts:admin-page')
    else:
        return redirect('useraccounts:user-dashboard')

@login_required
def admin_page_view(request):
    if request.user.email != 'test@gmail.com':
        return redirect('useraccounts:home')

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        if product_name:
            Product.objects.create(name=product_name)

    products = Product.objects.all()
    return render(request, 'admin_product_entry.html', {'products': products})

@login_required
def admin_dashboard_view(request):
    if request.user.email != 'test@gmail.com':
        return redirect('useraccounts:home')

    product_entries = ProductEntry.objects.all()
    return render(request, 'admin_database.html', {'product_entries': product_entries})

@login_required
def user_dashboard_view(request):
    if request.user.email == 'test@gmail.com':
        return redirect('useraccounts:admin-page')

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        weight = request.POST.get('weight')
        if product_id and weight:
            ProductEntry.objects.create(
                product_id=product_id,
                user=request.user,
                weight=weight
            )

    products = Product.objects.all()
    user_entries = ProductEntry.objects.filter(user=request.user).select_related('product', 'user')
    return render(request, 'user/dashboard.html', {
        'products': products,
        'user_entries': user_entries
    })

@login_required
def product_delete_view(request, pk):
    entry = get_object_or_404(ProductEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Product entry deleted successfully.')
        return redirect('useraccounts:user-dashboard')
    return render(request, 'user/product_confirm_delete.html', {'entry': entry})
