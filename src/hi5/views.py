from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from .models import product as product_model
from .models import productdetail as productdetail_model
from .models import category as category_model
from .models import Order as order_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateuserForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime

def home(request):
    #product_list= product_model.objects.filter().order_by('ID')    #select *from product

    p = Paginator(product_model.objects.filter().order_by('ID'), 8)
    default = request.GET.get('page')
    product_list = p.get_page(default)

    size_list = productdetail_model.objects.values_list('size',flat=True).distinct()
    color_list = productdetail_model.objects.values_list('color',flat=True).distinct()
    category_id_list = product_model.objects.values_list('categoryid',flat=True).distinct()
    category_name_list = category_model.objects.values_list('name',flat=True).filter(ID__in=category_id_list)

    
    categoryfind = request.GET.get('category')
    colorfind =  request.GET.get('color')
    sizefind =  request.GET.get('size')

    if categoryfind:
        p_id3 = category_model.objects.values('ID').filter(name=categoryfind)
        pid3 = Paginator(product_model.objects.filter(categoryid__in=p_id3), 8)
        product_list = pid3.get_page(categoryfind)

    elif colorfind:
        p_id2 = productdetail_model.objects.values('productid').filter(color=colorfind)
        pid2 = Paginator(product_model.objects.filter(ID__in=p_id2), 8)
        product_list = pid2.get_page(colorfind)
    elif sizefind:
        p_id = productdetail_model.objects.values('productid').filter(size=sizefind)
        pid = Paginator(product_model.objects.filter(ID__in=p_id), 8)
        product_list = pid.get_page(sizefind)
    else:
        product_list = p.get_page(default)

    context = {
       'product_list': product_list,
       'size_list': size_list,
       'color_list': color_list,
       'category_name_list': category_name_list
    }
    return render(request, 'hi5/dashboard.html',context)

def contact(request):
    # return HttpResponse('Products page')
    return render(request,'hi5/contact.html')
# Create your views here.

def guide(request):
    return render(request,'hi5/guide.html')

def guide_howto(request):
    return render(request,'hi5/how-to-make-purchase.html')

def guide_size(request):
    return render(request, 'hi5/size-guide.html')

def guide_payment(request):
    return render(request, 'hi5/payment.html')

def guide_warranty(request):
    return render(request, 'hi5/warranty.html')

def guide_tnc(request):
    return render(request, 'hi5/tnc.html')

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

def signuppage(request):
    if request.method == 'POST':
        # check if user exists
        try:
            user = User.objects.get(username=request.POST.get('username'))
            return render(request,'hi5/signup.html',messages.info(request, "Username Has Already Been Taken"))
            
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password'))
            user.save()
            messages.info(request, "Sign up successfully. Log In Again To Continue")
            return redirect('login')
            
    else:
        return render(request,'hi5/signup.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
    
def productitem(request):
    product_list= product_model.objects.filter().order_by('ID')
    productfind = request.GET.get('product')
    p_id = product_model.objects.filter(name=productfind)
    product = product_model.objects.filter(ID__in=p_id)
    context={
        'product_list': product_list,
        'product':product,
    }
    return render(request,'hi5/product-item.html',context)

def search(request):
    query = request.GET.get('query')
    product_list = product_model.objects.filter(name__icontains=query)
    context = {
       'product_list': product_list
    }
    return render(request,'hi5/search.html', context)


@login_required(login_url='/login')
def cart(request):
    cart_list = product_model.objects.filter(price = 400.0)

    context = {
        'cart_list': cart_list,
    }
    return render(request, "hi5/cart.html", context)

@login_required(login_url='/login')
def checkout(request):
    cart_list = product_model.objects.filter(price = 400.0)
    total = sum([item.price for item in product_model.objects.filter(price = 400.0)])

    context = {
        'cart_list': cart_list,
        'total': total
    }
    return render(request, "hi5/checkout.html", context)

def success(request):
    return render(request, "hi5/purchase_success.html")