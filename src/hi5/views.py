from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import product as product_model
def home(request):
    product_list= product_model.objects.filter().order_by('ID')    #select *from product
    return render(request, 'hi5/dashboard.html',{'product_list': product_list})
def contact(request):
    # return HttpResponse('Products page')
    return render(request,'hi5/contact.html')
# Create your views here.
def guide(request):
    return render(request,'hi5/guide.html')
def login(request):
    return render(request,'hi5/login.html')

    # Create your views here.
def productitem(request):
    return render(request,'hi5/product-item.html')
