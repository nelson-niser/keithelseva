from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Product(models.Model):
    product_seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField( max_length=30)
    price = models.IntegerField()
    description = models.CharField(null=True, blank=True, max_length=30)
    product_category = models.CharField(null=True, blank=True, max_length=30)
    # status = models.BooleanField(default=False)
    product_registration_date = models.DateField(null=True, blank=True)
    # links

    def __str__(self):
        return self.product_name + " | " + self.product_seller.username


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_seller','product_name','price','description','product_category','product_registration_date']
        labels  = {
        'product_seller':"I am",
        'product_name':'Item Name', 
        'price':'Price', 
        'description':'Description',
        'product_category':'Category',
        'product_registration_date':"Date Added"
        }
        widgets = {
        'product_seller': forms.Select(attrs={'class':'form-control'}),
        'product_name': forms.TextInput(attrs={'class':'form-control'}),
        'price': forms.NumberInput(attrs={'class':'form-control'}),
        'description': forms.TextInput(attrs={'class':'form-control'}),
        'product_category': forms.TextInput(attrs={'class':'form-control'}),
        'product_registration_date': forms.HiddenInput(),
        } 
