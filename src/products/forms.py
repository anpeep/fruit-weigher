# products/forms.py
from django import forms
from .models import Product, ProductEntry

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = ProductEntry
        fields = ['product', 'weight']
