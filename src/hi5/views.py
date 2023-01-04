from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import product as product_model
from .models import productdetail as productdetail_model
from .models import category as category_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateuserForm

def home(request):
    product_list= product_model.objects.filter().order_by('ID')    #select *from product
    size_list = productdetail_model.objects.values_list('size',flat=True).distinct()
    color_list = productdetail_model.objects.values_list('color',flat=True).distinct()
    category_id_list = product_model.objects.values_list('categoryid',flat=True).distinct()
    category_name_list = category_model.objects.values_list('name',flat=True).filter(ID__in=category_id_list)

    
    categoryfind = request.GET.get('category')
    colorfind =  request.GET.get('color')
    sizefind =  request.GET.get('size')

    if categoryfind:
        p_id3 = category_model.objects.values('ID').filter(name=categoryfind)
        product_list = product_model.objects.filter(categoryid__in=p_id3)

    elif colorfind:
        p_id2 = productdetail_model.objects.values('productid').filter(color=colorfind)
        product_list = product_model.objects.filter(ID__in=p_id2)

    elif sizefind:
        p_id = productdetail_model.objects.values('productid').filter(size=sizefind)
        product_list = product_model.objects.filter(ID__in=p_id)
    else:
        product_list = product_model.objects.filter().order_by('ID')


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
        form = CreateuserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'hi5/signup.html',{'form': form})
def PasswordForgot(request):
    return render(request,'hi5/ForgotPW.html')
def logoutpage(request):
    logout(request)
    return redirect('login')
def productitem(request):
    productfind = request.GET.get('product')
    p_id = product_model.objects.filter(name=productfind)
    product = product_model.objects.filter(ID__in=p_id)
    context={
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