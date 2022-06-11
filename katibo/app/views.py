import re
import pickle
import cgi, cgitb

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from matplotlib.style import context


from .forms import CreateUserForm
from .forms import CustomerForm
from .forms import CategoryForm
from .forms import ProductForm
from .forms import AddQtyForm
from .forms import SaleForm

from .models import *


# Create your views here.


def index(request):
    
    context = {}
    return render(request, 'index.html', context)

def sale(request):
    context = {}
    return render(request, 'sale.html', context)

def category(request):
    categories = Category.objects.all()


    pagination = Paginator(categories, 10)
    page_num = request.GET.get('page')
    pag_obj = pagination.get_page(page_num)

    context = {'pag_obj':pag_obj, 'categories':  categories}
    return render(request, 'category.html', context)

def product(request):

    products = Product.objects.all()


    pagination = Paginator(products, 10)
    page_num = request.GET.get('page')
    pag_obj = pagination.get_page(page_num)

    context = {'pag_obj':pag_obj, 'products': products}
    return render(request, 'product.html', context)

def add(request):
    add_prod = Add.objects.all()

    paginator = Paginator(add_prod, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj, 'add_prod': add_prod}
    return render(request, 'add.html', context)

def customer(request):
    customers = Customer.objects.all()

    pagination = Paginator(customers, 10)
    page_num = request.GET.get('page')
    pag_obj = pagination.get_page(page_num)

    context = {'pag_obj':pag_obj, 'customers': customers}
    return render(request, 'customer.html', context)

def report(request):
    reports = Sale.objects.all()
    
    pagination = Paginator(reports, 10)
    page_num = request.GET.get('page')
    pag_obj = pagination.get_page(page_num)

    context = {'pag_obj': pag_obj, 'reports': reports}
    return render(request, 'report.html', context)

#Artificial Intelligence Implementations
def anal(request):
    request.method = 'POST'
    a = request.POST['q1']
    if a == 'North-West':
        res1 = 1
    elif a == 'North-West':
        res1 = 2
    elif a == 'North-Central':
        res1 = 3
    elif a == 'South-South':
        res1 = 4
    elif a == 'South-East':
        res1 = 5
    else:
        res1 = 6
    
    
    res2 = request.POST['q2']
    res2 = int(res2)
    res3 = request.POST['q3']
    res3 = int(res3)
    res4 = request.POST['q4']
    res4 = int(res4)

    a = request.POST['q5']
    if a == 'Maize Corn':
        res5 = 1
    elif a == 'Yam Tuber':
        res5 = 2
    else:
        res5 = 3
    
    responses = [[res1, res2, res3, res4, res5]]
    #responses = list(map(int, responses))

    with open('yield_model.sav', 'rb') as f:
        model = pickle.load(f)
    
    y_pred = model.predict(responses)
    y_pred = int(y_pred)
    pred = 'Based on the provided information, your total yield for this year is'
    size = 'tonnes'
    context = {'pred': pred, 'y_pred': y_pred, 'size': size}
    return render(request, 'sell.html', context)

def sell_pred(request):
    return render(request, 'sell.html')

def prof_pred(request):
    request.GET
    context = {}
    return render(request, 'prof.html', context)

def analp(request):
    request.method = 'POST'
    a = request.POST['q1']
    if a == 'North-West':
        res1 = 1
    elif a == 'North-West':
        res1 = 2
    elif a == 'North-Central':
        res1 = 3
    elif a == 'South-South':
        res1 = 4
    elif a == 'South-East':
        res1 = 5
    else:
        res1 = 6
    
    
    res2 = request.POST['q2']
    res2 = int(res2)
    

    a = request.POST['q5']
    if a == 'Maize Corn':
        res5 = 1
    elif a == 'Yam Tuber':
        res5 = 2
    else:
        res5 = 3
    
    responses = [[res1, res5, res2,]]
    #responses = list(map(int, responses))

    with open('price_model.sav', 'rb') as f:
        model = pickle.load(f)
    
    y_pred = model.predict(responses)
    pred = 'Based on the provided information, your total yield for this year is'
    size = 'tonnes'
    context = {'pred': pred, 'y_pred': y_pred, 'size': size}
    return render(request, 'prof.html', context)

def types(request):
    context = {}
    return render(request, 'types.html', context)

def change(request):
    context ={}
    return render(request, 'change.html', context)

#Settings
def profile(request):
    context ={}
    return render(request, 'profile.html', context)

def login(request):
    context ={}
    return render(request, 'index.html', context)

def logout(request):
    context ={}
    return render(request, 'login.html', context)

#Forms creations
def  create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')

    context = {'form': form}

    return render(request, 'add_customer.html', context)

def  create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')

    context = {'form': form}

    return render(request, 'add_product.html', context)

def  create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')

    context = {'form': form}

    return render(request, 'add_category.html', context)
"""
def sale_item(request):
    formset = inlineformset_factory(Product, Sale)
    sale = Sale.objects.get(Product, 'prod_name')
    form = formset(queryset=Sale.objects.none())

    return render(request, 'add_sale.html', {'form': form})
"""

def add_qty(request, pk):
    product = Product.objects.get(id=pk)
    form = AddQtyForm(initial={'product': product})
    if request.method == "POST":
        form = AddQtyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    context = {'form': form}

    return render(request, 'add_qty.html', context)

def  sale_item(request):
    form = SaleForm()
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_item')

    context = {'form': form}

    return render(request, 'add_sale.html', context)

'''

def sale_item(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SaleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/sale/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SaleForm()

    return render(request, 'add_sale.html', {'form': form})
'''