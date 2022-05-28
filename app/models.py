from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import DateField

# Create your models her
class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    cus_name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cus_name

class Category(models.Model):
    cat_name = models.CharField(max_length=50, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    prod_name = models.CharField(max_length=50, null=True)
    prod_cat = models.ForeignKey(Category, db_column='cat_name', null=True, on_delete=models.SET_NULL)
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()
    prod_qty = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.prod_name

class Add(models.Model):
    prod_name = models.ForeignKey(Product, db_column='prod_name', null=True, on_delete=models.SET_NULL)
    prod_qty = models.IntegerField()
    nwe_price = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()

class Sale(models.Model):
    products = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.IntegerField()
    profit = models.IntegerField()
    date_created = DateField(auto_now_add=True)

    def __str__(self):
        return self.prod_cat
