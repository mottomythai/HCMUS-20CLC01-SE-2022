from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import product as product_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView

def home(request):
    product_list= product_model.objects.filter().order_by('ID')    #select *from product
    return render(request, 'hi5/dashboard.html',{'product_list': product_list})

def contact(request):
    # return HttpResponse('Products page')
    return render(request,'hi5/contact.html')
# Create your views here.
def guide(request):
    return render(request,'hi5/guide.html')
def infouserpage(request):
    return render(request,'hi5/userpage.html')
def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
        # Tài khoản hợp lệ
            login(request,user)
            return redirect('')
        else:
        # Tài khoản không hợp lệ
            messages.info(request, 'Username or Password is incorrect')
    context={}
    return render(request,'hi5/login.html',context)
def logoutpage(request):
    logout(request)
    return redirect('login')
def productitem(request):
    return render(request,'hi5/product-item.html')