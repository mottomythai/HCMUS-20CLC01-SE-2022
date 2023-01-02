from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from .models import account
from django.contrib import messages
from hi5.forms import accountForm, CreateuserForm

@login_required(login_url='login')
def infuser(request):
    username= request.user
    form =accountForm(instance=username)
    context={'form':form}
    return render(request,'hi5/userpage.html',context)

def PasswordChange(request):
    if request.method == 'POST':
        password_old = request.POST['passwordold']
        password_new = request.POST['passwordnew']
        password_confirm = request.POST['passwordconfirm']

        user = authenticate(request, username=request.user.username, password=password_old)
        if user is not None:
            if password_new == password_confirm:
                user.set_password(password_new)
                user.save()
                return redirect('')
            else:
                messages.info(request, 'Mật khẩu mới và xác nhận mật khẩu không khớp')
        else:
            messages.info(request, 'Mật khẩu cũ không đúng')
    context={}
    return render(request,'hi5/updatepw.html',context)


# Create your views here.
