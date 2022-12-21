from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'hi5/dashboard.html')
    # C:\Users\trang\Desktop\crm11\hi5\templates\acc\dashboard.html
    # return HttpResponse('Home page')
def contact(request):
    # return HttpResponse('Products page')
    return render(request,'hi5/contact.html')
def login(request):
    return render(request,'hi5/login.html')
# Create your views here.
def guide(request):
    return render(request,'hi5/guide.html')

    # Create your views here.
def product_item(request):
    return render(request,'hi5/product-item.html')