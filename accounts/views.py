from django.shortcuts import render
from django.http import HttpResponse

from . models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    content = {'orders': orders, 'customers' : customers }
    #orderStatus = 
    return render(request, 'accounts/dashboard.html',content)

def products(request):
    products = Product.objects.all()
    # we  can pass it into template by throwing in dictionary
    return render(request, 'accounts/products.html', {'products':products})
    

def customers(request):
    return render(request, 'accounts/customers.html')