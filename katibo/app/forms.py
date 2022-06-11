from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AddQtyForm(ModelForm):
    class Meta:
        model = Add
        fields = '__all__'

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class InsurForm(ModelForm):
    class Meta:
        model = Insurance
        fields = ['crop', 'type', 'predicted_harvest_quantity_in_tonnes', 'coverage_period_from', 'coverage_period_to']

class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ['claim_on', 'description']
'''
class SaleForm(forms.Form):
    product = forms.CharField(label='product', max_length=50)
    category = forms.CharField(label='category', max_length=50)
    buying = forms.IntegerField(label='buying')
    selling = forms.IntegerField(label='selling')
    quantity = forms.IntegerField(label='quantity')
    total = forms.IntegerField(label='total')
    profit = forms.IntegerField(label='profit')
    date = forms.DateField()
'''