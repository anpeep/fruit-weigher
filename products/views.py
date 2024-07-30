from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .models import Product, ProductEntry
from .forms import ProductForm, ProductEntryForm

@login_required
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(reverse("products:product-list"))
    return render(request, "product/product_form.html", {"form": form})

@login_required
def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse("products:product-detail", kwargs={"id": obj.id}))
    return render(request, "product/product_form.html", {"form": form, "object": obj})

@login_required
def product_delete_view(request, pk):
    entry = get_object_or_404(ProductEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete() 
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if AJAX request
            return JsonResponse({'success': True})
        else:
            messages.success(request, 'Product entry deleted successfully.')
            return redirect('useraccounts:user-dashboard')
    return render(request, 'user/product_confirm_delete.html', {'entry': entry})
