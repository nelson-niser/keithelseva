from django.shortcuts import render, redirect
from .models import Product, ProductForm
from django.utils.timezone import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_product(request):
    if request.method == 'POST':
        update_form = request.POST.copy()
        update_form.update({'product_registration_date':datetime.now().date()})
        form = ProductForm(update_form)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'add_product.html', {'ProductForm':ProductForm})