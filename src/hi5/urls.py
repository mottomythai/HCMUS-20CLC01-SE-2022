from django.contrib import admin
from . import views
from django.urls import path
from accouts import views as accout 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name=''),
    path("contact/", views.contact, name='contact'),
    path("login/", views.loginpage,name='login'),
    path("logout/", views.logoutpage,name='logout'),
    path("user/", accout.infuser,name='user'),
    path("guide/", views.guide,name='guide'),
    path("guide/how-to-make-purchase/", views.guide_howto, name='how-to-make-purchase'),
    path("guide/size-guide/", views.guide_size, name='size-guide'),
    path("guide/payment/", views.guide_payment, name='payment'),
    path("guide/warranty/", views.guide_warranty, name='warranty'),
    path("guide/tnc/", views.guide_tnc, name='t&c'),
    path("signup/", views.signuppage,name='signup'),
    path("product_item/", views.productitem,name='producitem'),
    path("password/", accout.PasswordChange,name='password'),
    path("reset_password/",auth_views.PasswordResetView.as_view(template_name='hi5/pw_reset.html'), name='reset_password'),
    path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name='hi5/pw_reset_send.html'), name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='hi5/pw_reset_confirm.html'), name='password_reset_confirm'),
    path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(template_name='hi5/pw_reset_done.html'), name='password_reset_complete'),
    path("search/",views.search,name='search'),
    #Cart
    path("cart/", views.cart, name='cart'),
    path("success/", views.success, name='success'),
    path("checkout/", views.checkout, name='checkout'),
]   
admin.site.site_header='Hi5'