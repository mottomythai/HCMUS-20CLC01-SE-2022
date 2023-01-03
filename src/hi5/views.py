from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import product as product_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from .models import category as category_model
#from .models import color as color_model
from .models import productdetail as productdetail_model

def home(request):
    product_list= product_model.objects.filter().order_by('ID')    #select *from product
    size_list = productdetail_model.objects.values_list('size',flat=True).distinct()
    color_list = productdetail_model.objects.values_list('color',flat=True).distinct()
    
    categoryfind = request.GET.get('category')
    
    if categoryfind:
        product_list = product_model.objects.filter(categoryid=categoryfind)
    else:
        product_list= product_model.objects.filter().order_by('ID')    #select *from product
    
    colorfind =  request.GET.get('color')
    if colorfind:
        p_id2 = productdetail_model.objects.values('productid').filter(color=colorfind)
        product_list = product_model.objects.filter(ID__in=p_id2)
    else:
        product_list = product_model.objects.filter().order_by('ID')

    sizefind =  request.GET.get('size')
    if sizefind:
        p_id = productdetail_model.objects.values('productid').filter(size=sizefind)
        product_list = product_model.objects.filter(ID__in=p_id)
    else:
        product_list = product_model.objects.filter().order_by('ID')


    context = {
       'product_list': product_list,
       'size_list': size_list,
       'color_list': color_list,
       #'productdetail_list': productdetail_list
    }

    return render(request, 'hi5/dashboard.html',context)

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

# def size(request,sizefind):
#     #sizefind =  request.GET.get('size')
#     if sizefind:
#         p_id = productdetail_model.objects.values('productid').filter(size=sizefind)
#         product_list = product_model.objects.filter(ID__in=p_id)
#     else:
#         product_list = product_model.objects.filter().order_by('ID')
#     return render(request, 'hi5/dashboard.html',{'product_list': product_list}) 