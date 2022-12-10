from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'hi5/dashboard.html')
    # C:\Users\trang\Desktop\crm11\hi5\templates\acc\dashboard.html
    # return HttpResponse('Home page')
def product(request):
    # return HttpResponse('Products page')
    return render(request,'hi5/products.html')
def customer(request):
    return render(request,'hi5/customer.html')
# Create your views here.
