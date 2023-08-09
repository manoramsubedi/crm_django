from django.shortcuts import render
from django.http import HttpResponse

from . models import *

#DASHBOARD
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers' : customers, 'total_orders': total_orders, 'delivered' : delivered ,'pending':pending}
    return render(request, 'accounts/dashboard.html',context)

#PRODUCT
def products(request):
    products = Product.objects.all()
    # we  can pass it into template by throwing in dictionary
    return render(request, 'accounts/products.html', {'products':products})
    
#CUSTOMERS
def customers(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders':orders, 'orders_count':orders_count}
    return render(request, 'accounts/customers.html', context)